from typing import Optional

import fastapi.exceptions
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from utils import RedisManager, generate_hash

# --------------

host = "192.168.0.115"  # TODO store as secrets
pwd = "foobared"

redis_manager = RedisManager(host=host, pwd=pwd)

print(redis_manager.list_keys())

# ---------------

app = FastAPI()


class GETLinkItem(BaseModel):
    id: str
    url: str
    description: Optional[str] = None


class POSTLinkItem(BaseModel):
    url: str
    description: Optional[str] = None


@app.get("api/id/{item_id}", response_model=GETLinkItem)
async def get_by_id(item_id: str):
    if redis_manager.exists_item(item_id):
        d = redis_manager.get_dict(item_id)

        return GETLinkItem(id=item_id, **d)
    raise fastapi.HTTPException(status_code=404, detail="No such link ID")


@app.post("api/shorten", response_model=GETLinkItem)
async def create_by_id(item: POSTLinkItem):
    item_id = generate_hash()
    redis_manager.set_dict(item_id, item.dict())

    x = GETLinkItem(id=item_id, **item.dict())
    return x


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
