from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None


class ItemCreate(ItemBase):
    title: str
    text: str


class Item(ItemCreate):
    id: str
