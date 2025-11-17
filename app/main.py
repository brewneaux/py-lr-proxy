from typing import Union

from fastapi import FastAPI
from . import litterbot

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/robots-statuses")
async def get_robot_statuses():
    return {x.name: x.status.name for x in await litterbot.get_robots()}
