from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.utils import redis_manager
from app import schemas

router = APIRouter(
    prefix='/api/item'
)

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="ID not found"
)

with_id = lambda m_id, d: schemas.ItemRetrieve(id=m_id, **d).dict()


@router.get('/{id}', response_model=schemas.Item)
async def get(id: str):
    if redis_manager.exists(id):
        d = redis_manager.get_dict(id)

        # return schemas.ItemRetrieve(id=id, **d)
        return with_id(id, d)

    raise not_found


@router.post('/', response_model=schemas.Item)
async def post(item: schemas.ItemCreate):
    d = item.dict()
    d.pop('id')

    redis_manager.set_dict(item.id, d)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=item.dict()
    )


@router.delete('/{id}', response_model=schemas.Item)
async def delete(id: str):
    if redis_manager.exists(id):
        d = redis_manager.get_dict(id)
        redis_manager.delete(id)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=with_id(id, d)
        )
    raise not_found


@router.get('/')
async def get_list():
    res = []
    for i in redis_manager.list_keys('*'):
        d = redis_manager.get_dict(i)
        # item = schemas.ItemRetrieve(id=i, **d)
        # res.append(item)
        res.append(with_id(i, d))

    return res
