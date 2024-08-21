import asyncio
import datetime
import functools
import json
import logging

import pytz
import websockets
from aiomqtt import Client, Will
from ocpp.routing import after, on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.datatypes import (
    ChargingProfile,
    ChargingSchedule,
    ChargingSchedulePeriod,
    IdTagInfo,
)
from ocpp.v16.enums import (
    Action,
    AuthorizationStatus,
    ChargePointErrorCode,
    ChargePointStatus,
    ChargingProfileKindType,
    ChargingProfilePurposeType,
    ChargingRateUnitType,
    RecurrencyKind,
    RegistrationStatus,
)
from transitions.extensions import AsyncMachine
from websockets.typing import Subprotocol

from .util import next_datetime_at_time

logger = logging.getLogger(__name__)

states = ["unknown", "disconnected", "idle", "active"]
transitions = [
    ["Available", ["unknown", "idle", "active"], "disconnected"],
    ["Available", "disconnected", None],
    ["Preparing", ["unknown", "disconnected", "active"], "idle"],
    ["Preparing", "idle", None],
    ["StartTransaction", ["unknown", "disconnected", "idle"], "active"],
    ["Charging", ["unknown", "disconnected", "idle"], "active"],
    ["Charging", "active", None],
    ["SuspendedEVSE", ["unknown", "disconnected", "idle"], "active"],
    ["SuspendedEVSE", "active", None],
    ["SuspendedEV", ["unknown", "disconnected", "idle"], "active"],
    ["SuspendedEV", "active", None],
    ["Finishing", ["unknown", "disconnected", "idle"], "active"],
    ["Finishing", "active", None],
]

default_machine = AsyncMachine(
    states=states,
    transitions=transitions,
    initial="unknown",
    after_state_change="on_state_change",
)


class MyChargePoint(cp):
    def __init__(self, id, connection, mqtt_client: Client, response_timeout=30):  # noqa: A002
        self.logger = logging.getLogger(f"{__name__}.{id}")
        self.mqtt_client = mqtt_client

        super().__init__(id, connection, response_timeout)

    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor: str, charge_point_model: str, **kwargs
    ):
        self.logger.debug(
            "Boot from %s %s",
            charge_point_vendor,
            charge_point_model,
        )

        await self.mqtt_client.publish(
            f"ocpp/{self.id}/boot",
            json.dumps({"vendor": charge_point_vendor, "model": charge_point_model}),
        )

        return call_result.BootNotification(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @after(Action.BootNotification)
    async def after_boot_notification(self, **kwargs) -> None:
        result: call_result.SetChargingProfile = await self.call(
            call.SetChargingProfile(
                connector_id=0,
                cs_charging_profiles=ChargingProfile(
                    charging_profile_id=1,
                    stack_level=1,
                    charging_profile_purpose=ChargingProfilePurposeType.tx_default_profile,
                    charging_profile_kind=ChargingProfileKindType.recurring,
                    recurrency_kind=RecurrencyKind.daily,
                    charging_schedule=ChargingSchedule(
                        ChargingRateUnitType.watts,
                        [
                            ChargingSchedulePeriod(0, 7200),
                        ],
                        duration=18000,
                        start_schedule=next_datetime_at_time(
                            datetime.time(0, 30, tzinfo=pytz.timezone("Europe/London"))
                        ).isoformat(),
                    ),
                ),
            )
        )

        self.logger.debug("Charging profile set: %s", result.status)

    @on(Action.heartbeat)
    async def on_heartbeat(self):
        self.logger.debug("Heartbeat")

        await self.mqtt_client.publish(
            f"ocpp/{self.id}/heartbeat", datetime.datetime.now(datetime.UTC).isoformat()
        )

        return call_result.Heartbeat(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
        )

    @on(Action.status_notification)
    async def on_status_notification(
        self,
        connector_id: int,
        error_code: ChargePointErrorCode,
        status: ChargePointStatus,
        **kwargs,
    ):
        self.logger.debug(
            "Status: connector %d %s %s",
            connector_id,
            error_code,
            status,
        )

        await self.mqtt_client.publish(f"ocpp/{self.id}/connector_status", status)

        return call_result.StatusNotification()

    @after(Action.status_notification)
    async def after_status_notification(
        self,
        connector_id: int,
        error_code: ChargePointErrorCode,
        status: ChargePointStatus,
        **kwargs,
    ):
        await self.trigger(status)  # type:ignore[attr-defined]

    async def on_state_change(self):
        await self.mqtt_client.publish(f"ocpp/{self.id}/state", self.state)

    @on(Action.start_transaction)
    async def on_start_transaction(
        self,
        connector_id: int,
        id_tag: str,
        meter_start: int,
        timestamp: str,
        reservation_id: int | None = None,
        **kwargs,
    ):
        self.logger.debug("Transaction started")

        return call_result.StartTransaction(
            1, id_tag_info=IdTagInfo(AuthorizationStatus.accepted)
        )

    async def on_enter_idle(self) -> None:
        result: call_result.RemoteStartTransaction = await self.call(
            call.RemoteStartTransaction("noIdTag")
        )
        self.logger.debug("Remote start: %s", result.status)

    async def mqtt_consumer(self) -> None:
        await self.mqtt_client.subscribe(f"ocpp/{self.id}/charge_limit")

        async for message in self.mqtt_client.messages:
            self.logger.debug(
                "Recieved mqtt message on %s: %s", message.topic, message.payload
            )

            if message.topic.value == f"ocpp/{self.id}/charge_limit":
                await self.set_baseline_power_limit(
                    int(float(str(message.payload.decode())))
                )

    async def set_baseline_power_limit(self, limit: int) -> None:
        result: call_result.SetChargingProfile = await self.call(
            call.SetChargingProfile(
                connector_id=0,
                cs_charging_profiles=ChargingProfile(
                    charging_profile_id=2,
                    stack_level=0,
                    charging_profile_purpose=ChargingProfilePurposeType.tx_default_profile,
                    charging_profile_kind=ChargingProfileKindType.absolute,
                    charging_schedule=ChargingSchedule(
                        ChargingRateUnitType.watts,
                        [
                            ChargingSchedulePeriod(0, limit),
                        ],
                    ),
                ),
            )
        )

        self.logger.debug("Set baseline profile to %d W: %s", limit, result.status)

    @on(Action.meter_values)
    async def on_meter_values(self, connector_id, meter_value, **kwargs):
        self.logger.debug("Meter Values: %r", meter_value)
        return call_result.MeterValues()

    @after(Action.meter_values)
    async def after_meter_values(self, connector_id, meter_value, **kwargs):
        for sample in meter_value["sampled_value"]:
            await self.mqtt_client.publish(
                f"ocpp/{self.id}/{sample['measurand']}", sample["value"]
            )


async def on_connect(websocket, path, mqtt_client):
    """For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = path.strip("/").split("/")[-1]
    cp = MyChargePoint(charge_point_id, websocket, mqtt_client)

    default_machine.add_model(cp)

    logger.debug("CP %s connected", charge_point_id)

    try:
        await asyncio.gather(cp.start(), cp.mqtt_consumer())
    except websockets.exceptions.ConnectionClosedOK:
        logger.debug("CP %s disconnected", charge_point_id)


async def start_ocpp(mqtt_client: Client):
    handler = functools.partial(on_connect, mqtt_client=mqtt_client)

    server = await websockets.serve(
        handler,
        "0.0.0.0",
        9000,
        subprotocols=[Subprotocol("ocpp1.6")],
    )

    await server.wait_closed()


async def main():
    async with Client(
        "mqtt.home.larkspur.me.uk", will=Will("ocpp/online", "OFF")
    ) as client:
        await client.publish("ocpp/online", "ON")
        await start_ocpp(client)
