import datetime
import logging

import websockets
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16.enums import Action, RegistrationStatus


class MyChargePoint(cp):
    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor, charge_point_model, **kwargs
    ):
        return call_result.BootNotification(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @on(Action.heartbeat)
    async def on_heartbeat(self):
        return call_result.Heartbeat(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
        )


async def on_connect(websocket, path):
    """For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = path.strip("/")
    cp = MyChargePoint(charge_point_id, websocket)

    logging.debug("CP %s connected", charge_point_id)
    print("[CS] CP Connected")
    await cp.start()
    print("[CS] Started")


async def main():
    server = await websockets.serve(
        on_connect, "0.0.0.0", 9000, subprotocols=["ocpp1.6"]
    )

    await server.wait_closed()
