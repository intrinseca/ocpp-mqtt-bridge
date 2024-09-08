import functools
import logging

import websockets

from .central_station import CentralStation
from .mqtt import MQTTInterface
from .ocpp_interface import OCPPInterface

logger = logging.getLogger(__name__)


async def on_connect(
    websocket: websockets.WebSocketServerProtocol,
    mqtt_hostname: str,
    mqtt_prefix: str,
):
    """For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = websocket.path.strip("/").split("/")[-1]

    ocpp = OCPPInterface(charge_point_id, websocket)
    mqtt = MQTTInterface(charge_point_id, mqtt_hostname, mqtt_prefix)

    cs = CentralStation(ocpp, mqtt)

    logger.debug("CP %s connected", charge_point_id)

    try:
        await cs.start()
    except websockets.exceptions.ConnectionClosedOK:
        logger.debug("CP %s disconnected", charge_point_id)


async def start_ocpp(mqtt_hostname: str, mqtt_prefix: str):
    handler = functools.partial(
        on_connect, mqtt_hostname=mqtt_hostname, mqtt_prefix=mqtt_prefix
    )

    server = await websockets.serve(
        handler,
        "0.0.0.0",
        9000,
        subprotocols=[websockets.Subprotocol("ocpp1.6")],
    )

    await server.wait_closed()
