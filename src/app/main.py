from typing import Union
import logging
import sys
from fastapi import FastAPI, HTTPException
from app import litterbot
from .config import Settings


settings = Settings()
app = FastAPI()

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/robots-statuses")
async def get_robot_statuses():
    return await litterbot.get_robots()


@app.get("/monitors")
async def get_monitors():
    from app.monitors import get_all_monitors

    return await get_all_monitors()

@app.get("/list-monitors")
def list_monitors():
    from app.monitors import MONITORS
    return [x().monitor_name for x in MONITORS]

@app.get("/monitor/{monitor_name}")
def get_single_monitor(monitor_name: str):
    from app.monitors import MONITORS
    matching_monitors = [x().monitor_name for x in MONITORS if x().monitor_name == monitor_name]
    if not matching_monitors:
        raise HTTPException(status_code=400, detail="Monitor not found")
    m = matching_monitors[0]
    return m().get_status()