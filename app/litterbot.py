import os
from pylitterbot import Account, LitterRobot
from typing import List
import logging
import sys

USERNAME = os.environ.get("WHISKER_USERNAME")
PASSWORD = os.environ.get("WHISKER_PASSWORD")

if not (USERNAME and PASSWORD):
    raise EnvironmentError("Must set WHISKER_USERNAME and WHISKER_PASSWORD")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)


async def get_robots() -> List[LitterRobot]:
    # Create an account.
    logger.debug("Creating account")
    account = Account()

    try:
        # Connect to the API and load robots.
        logger.debug("Connecting")
        await account.connect(username=USERNAME, password=PASSWORD, load_robots=True)
        logger.info("Connected, returning robots")
        return [x for x in account.robots if isinstance(x, LitterRobot)]
    finally:
        # Disconnect from the API.
        await account.disconnect()
