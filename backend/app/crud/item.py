from app.schemas import Item, ItemCreate
from app.crud.base import CRUDBase

from app.utils import redis_manager


class CRUDItem(CRUDBase[Item, ItemCreate]):
    pass


item = CRUDItem(Item, redis_manager)
