from typing import Optional

from fastapi import FastAPI
import fastapi.exceptions
from pydantic import BaseModel
from utils import RedisManager, generate_hash

host = "192.168.0.115"  # TODO store as secrets
pwd = "foobared"

redis_manager = RedisManager(host=host, pwd=pwd)

app = FastAPI()


class GetModel(BaseModel):
    id: str
    name: str
    description: Optional[str]


ITEM_ENDPOINT = '/api/item'
PING_ENDPOINT = '/api/ping'


@app.get(ITEM_ENDPOINT + '/{id}', response_model=GetModel)
async def get(id: str):
    if redis_manager.exists(id):
        d = redis_manager.get_dict(id)

        return GetModel(id=id, **d)
    raise fastapi.HTTPException(status_code=404, detail="id not found")


@app.post(ITEM_ENDPOINT)
async def post(item: GetModel):
    d = item.dict()
    d.pop('id')

    redis_manager.set_dict(item.id, d)

    return fastapi.Response('ok', 201)


@app.get(PING_ENDPOINT)
async def ping():
    return fastapi.Response('ok', 200)
