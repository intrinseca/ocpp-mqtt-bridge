import asyncio
import logging.config
import os
import sys
import tomllib

import click

from .websocket import start_ocpp


@click.command()
@click.option("--hostname", "-h", required=True, help="The hostname of the MQTT server")
@click.option("--prefix", "-p", default="ocpp", help="MQTT topic prefix")
def main(hostname: str, prefix: str) -> None:
    os.makedirs("logs", exist_ok=True)

    with open("logging_config.toml", "rb") as logging_config_file:
        logging_config = tomllib.load(logging_config_file)

    logging.config.dictConfig(logging_config)

    # Change to the "Selector" event loop if platform is Windows
    if sys.platform.lower() == "win32" or os.name.lower() == "nt":
        from asyncio import WindowsSelectorEventLoopPolicy, set_event_loop_policy

        set_event_loop_policy(WindowsSelectorEventLoopPolicy())

    asyncio.run(start_ocpp(hostname, prefix))


if __name__ == "__main__":
    main()
