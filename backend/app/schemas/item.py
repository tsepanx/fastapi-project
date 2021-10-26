from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None


class ItemCreate(ItemBase):
    id: str  # hash
    title: str
    text: str


class Item(ItemCreate):
    pass


class ItemRetrieve(ItemCreate):
    pass
