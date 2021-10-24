from typing import Optional

from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from pydantic import BaseModel

from backend.utils import ok_status, RedisManager

host = "192.168.0.115"  # TODO store as secrets
pwd = "foobared"

redis_manager = RedisManager(host=host, pwd=pwd)

router = APIRouter(
    prefix='/api/item'
)


class GetModel(BaseModel):
    id: str
    name: str
    description: Optional[str]


@router.get('/{id}', response_model=GetModel)
async def get(id: str):
    if redis_manager.exists(id):
        d = redis_manager.get_dict(id)

        return GetModel(id=id, **d)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ID not found"
    )


@router.post('/')
async def post(item: GetModel):
    d = item.dict()
    d.pop('id')

    redis_manager.set_dict(item.id, d)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=ok_status
    )
