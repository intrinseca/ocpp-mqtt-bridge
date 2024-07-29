import argparse
import asyncio
import logging

import websockets
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call
from ocpp.v16.enums import RegistrationStatus

logging.basicConfig(level=logging.INFO)


class ChargePointSimulator(cp):
    async def send_boot_notification(self):
        request = call.BootNotification(
            charge_point_serial_number=arguments["cp_serial"],
            charge_point_model=arguments["cp_model"],
            charge_point_vendor=arguments["cp_vendor"],
            firmware_version=arguments["cp_version"],
        )
        response = await self.call(request)

        if response.status == RegistrationStatus.accepted:
            logging.info("%s: connected to central system", arguments["cp_id"])
            if response.interval:
                arguments["heartbeat_interval"] = response.interval
                logging.info(
                    "%s: heartbeat interval set to %s",
                    arguments["cp_id"],
                    response.interval,
                )

        return True

    async def send_commands(self, arguments):
        await self.send_boot_notification()
        await self.send_heartbeats(arguments)

    async def send_heartbeats(self, arguments):
        while True:
            request = call.Heartbeat()
            await self.call(request)
            await asyncio.sleep(arguments["heartbeat_interval"])


async def main(arguments):
    try:
        async with websockets.connect(
            f"{arguments['url']}/{arguments['cp_id']}",
            subprotocols=["ocpp1.6"],
        ) as ws:
            cp = ChargePointSimulator(arguments["cp_id"], ws)
            await asyncio.gather(cp.start(), cp.send_commands(arguments))
    except Exception as e:
        logging.error("%s: %s", arguments["cp_id"], e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="The CS URL", required=True)
    parser.add_argument(
        "--cp-id", help="The Charge Point ID", default="CP1", required=False
    )
    parser.add_argument(
        "--cp-model",
        help="The Change Point model",
        default="CHARGE_POINT_MODEL",
        required=False,
    )
    parser.add_argument(
        "--cp-vendor",
        help="The Change Point vendor name",
        default="CHARGE_POINT_VENDOR",
        required=False,
    )
    parser.add_argument(
        "--cp-version",
        help="The Change Point firmware version",
        default="1.2.3.4",
        required=False,
    )
    parser.add_argument(
        "--cp-serial",
        help="The Change Point serial number",
        default="CP1234567890A01",
        required=False,
    )

    arguments = vars(parser.parse_args())
    asyncio.run(main(arguments))
