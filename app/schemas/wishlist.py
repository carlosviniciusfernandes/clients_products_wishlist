from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator

from controllers.product import ProductController


class WishlistItemBase(BaseModel):
    product_id: str
    owner_id: str


class WishlistItemCreate(WishlistItemBase):
    @validator("product_id")
    def validate_if_product_exists(cls, value):
        if ProductController().does_product_exists(value):
            return value
        else:
            raise ValidationError


class WishlistItem(WishlistItemBase):
    id: str

    class Config:
        orm_mode = True


class WishlistItemDetailed(BaseModel):
    id: str
    title: str
    brand: str
    image: str
    price: float
    reviewScore: Optional[str]

    def __init__(self, wishlist_item: WishlistItem):
        item_details = ProductController().does_product_exists(wishlist_item.product_id)
        if item_details:
            for detail, value in item_details.items():
                self.__dict__[detail] = value

    class Config:
        orm_mode = True


class WishlistDetailed(BaseModel):
    __root__: List[WishlistItemDetailed]

    class Config:
        orm_mode = True
