from typing import Optional

import fastapi.exceptions
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from utils import RedisManager, gen_id

# -------

host = "192.168.0.115"
pwd = "foobared"

redis_manager = RedisManager(host=host, pwd=pwd)

x = redis_manager.list_keys()
print(x)
print(gen_id(20))

# ---------------

app = FastAPI()


class GETLinkItem(BaseModel):
    id: str
    url: str
    description: Optional[str] = None


class POSTLinkItem(BaseModel):
    url: str
    description: Optional[str] = None


@app.get("/id/{link_id}", response_model=GETLinkItem)
async def get_by_id(link_id: str):
    if redis_manager.exists_item(link_id):
        url = redis_manager.get_item(link_id)

        return GETLinkItem(id=link_id, url=url)  # TODO store links fields as separate redis-hash dict

    raise fastapi.HTTPException(status_code=404, detail="No such link ID")


@app.post("/shorten", response_model=GETLinkItem)
async def create_by_id(item: POSTLinkItem):
    link_id = gen_id()
    redis_manager.set_item(link_id, item.url)

    return GETLinkItem.construct(**item.dict(), id=link_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
