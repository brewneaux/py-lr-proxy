from pylitterbot import Account, LitterRobot
from typing import List, Dict
from app.config import settings
import logging


async def get_robots() -> List[Dict]:
    # Create an account.
    logger = logging.getLogger(__name__)
    logger.debug("Creating account")
    account = Account()

    s = settings()
    USERNAME = s.whisker_username
    PASSWORD = s.whisker_password

    try:
        # Connect to the API and load robots.
        logger.debug("Connecting")
        await account.connect(username=USERNAME, password=PASSWORD, load_robots=True)
        logger.info("Connected, returning robots")
        return [parse_litterrobot_status(x) for x in account.robots if isinstance(x, LitterRobot)]
    finally:
        # Disconnect from the API.
        await account.disconnect()


def parse_litterrobot_status(robot: LitterRobot) -> Dict:
    return {
        "drawerGettingFull": robot.waste_drawer_level > 70,
        "status": robot.status.name,
        "model": robot.model,
        "name": robot.name,
    }
