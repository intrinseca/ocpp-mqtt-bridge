import asyncio
import datetime
import functools
import json
import logging

import websockets
from aiomqtt import Client
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
    MessageTrigger,
    RecurrencyKind,
    RegistrationStatus,
)
from transitions.extensions import AsyncMachine
from websockets.typing import Subprotocol
from zoneinfo import ZoneInfo

from .mqtt import HAMQTTClient, Number, Sensor
from .util import today_at

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
    def __init__(self, id, connection, mqtt_client: HAMQTTClient, response_timeout=30):  # noqa: A002
        self.logger = logging.getLogger(f"{__name__}.{id}")
        self.mqtt_client = mqtt_client

        super().__init__(id, connection, response_timeout)

        self.charging_limit_number = Number(
            self.id, "charging_limit", set_handler=self.set_baseline_power_limit
        )

        self.boot_sensor = Sensor(self.id, "boot")
        self.heartbeat_sensor = Sensor(self.id, "heartbeat")
        self.connector_status_sensor = Sensor(self.id, "connector_status")
        self.state_sensor = Sensor(self.id, "state")
        self.energy_meter_sensor = Sensor(self.id, "energy_meter")
        self.power_sensor = Sensor(self.id, "power")

    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor: str, charge_point_model: str, **kwargs
    ):
        self.logger.debug(
            "Boot from %s %s",
            charge_point_vendor,
            charge_point_model,
        )

        await self.mqtt_client.register(self.charging_limit_number)
        await self.mqtt_client.register(self.boot_sensor)
        await self.mqtt_client.register(self.heartbeat_sensor)
        await self.mqtt_client.register(self.connector_status_sensor)
        await self.mqtt_client.register(self.state_sensor)
        await self.mqtt_client.register(self.energy_meter_sensor)
        await self.mqtt_client.register(self.power_sensor)

        await self.boot_sensor.publish(
            json.dumps({"vendor": charge_point_vendor, "model": charge_point_model})
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
                        start_schedule=today_at(
                            datetime.time(0, 30, tzinfo=ZoneInfo("Europe/London"))
                        ).isoformat(),
                    ),
                ),
            )
        )

        self.logger.debug("Charging profile set: %s", result.status)

    @on(Action.heartbeat)
    async def on_heartbeat(self):
        self.logger.debug("Heartbeat")

        await self.heartbeat_sensor.publish(
            datetime.datetime.now(datetime.UTC).isoformat()
        )

        return call_result.Heartbeat(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
        )

    @after(Action.heartbeat)
    async def after_heartbeat(self) -> None:
        result: call_result.GetCompositeSchedule = await self.call(
            call.GetCompositeSchedule(
                connector_id=1,
                duration=60 * 60 * 24,
                charging_rate_unit=ChargingRateUnitType.watts,
            )
        )

        self.logger.info(
            "Composite Schedule: %s %r", result.status, result.charging_schedule
        )

        trigger_result: call_result.TriggerMessage = await self.call(
            call.TriggerMessage(MessageTrigger.meter_values)
        )

        self.logger.debug("Requested meter values: %s", trigger_result.status)

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

        await self.connector_status_sensor.publish(status)

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
        await self.state_sensor.publish(self.state)

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
        await self.charging_limit_number.publish(limit)

    @on(Action.meter_values)
    async def on_meter_values(self, connector_id, meter_value, **kwargs):
        self.logger.debug("Meter Values: %r", meter_value)
        return call_result.MeterValues()

    @after(Action.meter_values)
    async def after_meter_values(self, connector_id, meter_value, **kwargs):
        latest_sample = max(meter_value, key=lambda m: m["timestamp"])

        for value in latest_sample["sampled_value"]:
            if value["measurand"] == "Energy.Active.Import.Register":
                await self.energy_meter_sensor.publish(value["value"])
            elif value["measurand"] == "Power.Active.Import":
                await self.power_sensor.publish(value["value"])


async def on_connect(websocket, path, mqtt_client):
    """For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = path.strip("/").split("/")[-1]
    cp = MyChargePoint(charge_point_id, websocket, mqtt_client)

    default_machine.add_model(cp)

    logger.debug("CP %s connected", charge_point_id)

    try:
        await cp.start()
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


async def run_cs(hostname, prefix):
    client = HAMQTTClient(prefix=prefix, hostname=hostname)
    await asyncio.gather(client.connect(), start_ocpp(client))
