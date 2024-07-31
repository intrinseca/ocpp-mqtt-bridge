import asyncio
import datetime
import logging

import websockets
from ocpp.routing import after, on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.enums import (
    Action,
    ChargePointErrorCode,
    ChargePointStatus,
    RegistrationStatus,
)
from transitions.extensions import AsyncMachine

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
)


class MyChargePoint(cp):
    def __init__(self, id, connection, response_timeout=30):  # noqa: A002
        self.logger = logging.getLogger(f"{__name__}.{id}")
        super().__init__(id, connection, response_timeout)

        self.action_queue = asyncio.Queue()

    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor: str, charge_point_model: str, **kwargs
    ):
        self.logger.debug(
            "Received boot, %s %s",
            charge_point_vendor,
            charge_point_model,
        )
        return call_result.BootNotification(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @on(Action.heartbeat)
    async def on_heartbeat(self):
        self.logger.debug("Received heartbeat")
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
            "Received status notification, connector %d %s %s",
            connector_id,
            error_code,
            status,
        )

        return call_result.StatusNotification()

    @after(Action.status_notification)
    async def after_status_notification(
        self,
        connector_id: int,
        error_code: ChargePointErrorCode,
        status: ChargePointStatus,
        **kwargs,
    ):
        self.logger.debug(
            "After status notification, connector %d %s %s",
            connector_id,
            error_code,
            status,
        )

        # await self.trigger(status)  # type:ignore[attr-defined]
        result: call_result.RemoteStartTransaction = await self.call(
            call.RemoteStartTransaction("noIdTag")
        )
        self.logger.debug("Remote start %s", result.status)

    async def on_enter_idle(self) -> None:
        self.logger.debug("Entering idle, queueing RemoteStartTransaction")
        await self.action_queue.put("RemoteStart")

    async def queue_consumer(self) -> None:
        while True:
            action = await self.action_queue.get()
            self.logger.debug("[Action Queue] %s", action)
            match action:
                case "RemoteStart":
                    result: call_result.RemoteStartTransaction = await self.call(
                        call.RemoteStartTransaction("noIdTag")
                    )
                    self.logger.debug("Remote start %s", result.status)


async def on_connect(websocket, path):
    """For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = path.strip("/")
    cp = MyChargePoint(charge_point_id, websocket)

    default_machine.add_model(cp)

    logger.debug("CP %s connected", charge_point_id)

    try:
        await asyncio.gather(cp.start(), cp.queue_consumer())
    except websockets.exceptions.ConnectionClosedOK:
        logger.debug("CP %s disconnected", charge_point_id)


async def main():
    server = await websockets.serve(
        on_connect, "0.0.0.0", 9000, subprotocols=["ocpp1.6"]
    )

    await server.wait_closed()
