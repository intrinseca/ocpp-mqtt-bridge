import asyncio
import logging.config
import os
import sys

import tomllib

from .cs import main

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)

    with open("logging_config.toml", "rb") as logging_config_file:
        logging_config = tomllib.load(logging_config_file)

    logging.config.dictConfig(logging_config)

    # Change to the "Selector" event loop if platform is Windows
    if sys.platform.lower() == "win32" or os.name.lower() == "nt":
        from asyncio import WindowsSelectorEventLoopPolicy, set_event_loop_policy

        set_event_loop_policy(WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
