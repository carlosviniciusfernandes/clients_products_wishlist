from typing import List
from pydantic import BaseModel


class WishlistItemBase(BaseModel):
    product_id: str
    owner_id: str


class WishlistItemCreate(WishlistItemBase):
    pass


class WishlistItem(WishlistItemCreate):
    id: int

    class Config:
        orm_mode = True


class Wishlist(BaseModel):
    __root__: List[WishlistItem]
