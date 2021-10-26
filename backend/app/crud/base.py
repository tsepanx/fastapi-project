from typing import TypeVar, Type, Generic

from pydantic import BaseModel

from app.utils import RedisManager

BaseSchemaType = TypeVar("BaseSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


def prepare_id(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]

        key = f'{self.prefix}:{id}'

        d = func(self, key, *args[2:], **kwargs)

        if 'id' in d.dict():
            if (pos := d.id.find(':')) != -1:
                d.id = d.id[pos+1:]

        return d

    return wrapper


class CRUDBase(Generic[BaseSchemaType, CreateSchemaType]):
    def __init__(self, model: Type[BaseSchemaType], redis: RedisManager):
        self.model = model
        self.prefix = self.model.__name__
        self.redis = redis

    @prepare_id
    def get(self, id: str) -> BaseSchemaType:
        if self.redis.exists(id):
            h_dict = self.redis.get_dict(id)

            return self.model.construct(**h_dict)
        raise KeyError

    @prepare_id
    def create(self, id: str, obj_in: CreateSchemaType) -> BaseSchemaType:
        h_dict = obj_in.dict()
        h_dict.update({'id': id})

        self.redis.set_dict(id, h_dict)

        return self.model.construct(**self.redis.get_dict(id))

    def remove(self, id: str) -> BaseSchemaType:
        if self.redis.exists(id):
            d = self.redis.get_dict(id)
            self.redis.delete(id)

            return d

        raise KeyError
