import datetime
import logging

import websockets
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16.enums import (
    Action,
    ChargePointErrorCode,
    ChargePointStatus,
    RegistrationStatus,
)

logger = logging.getLogger(__name__)


class MyChargePoint(cp):
    def __init__(self, id, connection, response_timeout=30):  # noqa: A002
        self.logger = logging.getLogger(f"{__name__}.{id}")
        super().__init__(id, connection, response_timeout)

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


async def on_connect(websocket, path):
    """For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = path.strip("/")
    cp = MyChargePoint(charge_point_id, websocket)

    logger.debug("CP %s connected", charge_point_id)

    try:
        await cp.start()
    except websockets.exceptions.ConnectionClosedOK:
        logger.debug("CP %s disconnected", charge_point_id)


async def main():
    server = await websockets.serve(
        on_connect, "0.0.0.0", 9000, subprotocols=["ocpp1.6"]
    )

    await server.wait_closed()
