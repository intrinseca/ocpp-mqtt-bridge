import asyncio
import logging
import os
import sys

from .cs import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # Change to the "Selector" event loop if platform is Windows
    if sys.platform.lower() == "win32" or os.name.lower() == "nt":
        from asyncio import WindowsSelectorEventLoopPolicy, set_event_loop_policy

        set_event_loop_policy(WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
