from fastapi import FastAPI
import fastapi.exceptions
from pydantic import BaseModel
from utils import RedisManager, generate_hash

host = "192.168.0.115"  # TODO store as secrets
pwd = "foobared"

redis_manager = RedisManager(host=host, pwd=pwd)


class GETModel(BaseModel):
    destination: str


class POSTModel(BaseModel):
    destination: str
    domain: str


class POSTResponseModel(BaseModel):
    id: str
    short_url: str


LINK_ENDPOINT = '/api/url'

GET_ENDPOINT = f'{LINK_ENDPOINT}/{{id}}'
POST_ENDPOINT = LINK_ENDPOINT

app = FastAPI()


@app.get(GET_ENDPOINT, response_model=GETModel)
async def get(id: str):
    if redis_manager.exists_item(id):
        d = redis_manager.get_dict(id)

        return GETModel(id=id, **d)
    raise fastapi.HTTPException(status_code=404, detail="No such link ID")


@app.post(POST_ENDPOINT, response_model=POSTResponseModel)
async def post(item: POSTModel):
    item_id = generate_hash()
    redis_manager.set_dict(item_id, item.dict())

    res_url = item.domain + '/' + item_id

    return POSTResponseModel.construct(id=item_id, short_url=res_url)
