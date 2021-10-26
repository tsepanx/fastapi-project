from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.crud.item import item
from app import schemas, utils

router = APIRouter(
    prefix='/api/item'
)

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="ID not found"
)


@router.get('/{id}', response_model=schemas.Item)
async def get(id: str):
    try:
        return item.get(id)
    except KeyError:
        raise not_found


@router.post('/', response_model=schemas.Item)
async def post(item_in: schemas.ItemCreate):
    item_id = utils.generate_id()

    item_db = item.create(item_id, item_in)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=item_db.dict()
    )


@router.delete('/{id}', response_model=schemas.Item)
async def delete(id: str):
    try:
        item_db = item.remove(id)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=item_db.dict()
        )
    except KeyError:
        raise not_found


# @router.get('/')
# async def get_list():
#     res = []
#     for i in redis_manager.list_keys('*'):
#         d = redis_manager.get_dict(i)
#         res.append(with_id(i, d))
#
#     return res
