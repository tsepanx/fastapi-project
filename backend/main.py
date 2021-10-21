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


class GETModel(BaseModel):
    id: str
    url: str
    description: Optional[str] = None


class POSTModel(BaseModel):
    url: str
    description: Optional[str] = None


item_endpoint = '/api/item/'


@app.get(item_endpoint, response_model=GETModel)
async def get_by_id(id: str):
    if redis_manager.exists_item(id):
        d = redis_manager.get_dict(id)

        return GETModel(id=id, **d)
    raise fastapi.HTTPException(status_code=404, detail="No such link ID")


@app.post(item_endpoint, response_model=GETModel)
async def create_by_id(item: POSTModel):
    item_id = generate_hash()
    redis_manager.set_dict(item_id, item.dict())

    return GETModel(id=item_id, **item.dict())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
