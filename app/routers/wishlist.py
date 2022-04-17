import json
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from auth import current_active_user
from controllers.wishlist import WishlistController
from schemas.user import User
from schemas.wishlist import WishlistDetailed, WishlistItemCreate, WishlistItem, WishlistItemDetailed

wishlist_router = APIRouter(
    prefix="/wishlist",
    tags=['wishlist']
)


@wishlist_router.post(
    "/{product_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=WishlistItem
)
async def add_item_to_user_withlist(product_id: str, user: User = Depends(current_active_user)):
    try:
        wishlist_item = WishlistItemCreate(product_id=product_id, owner_id=str(user.id))
        return await WishlistController().add_item_to_wishlist(wishlist_item)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Product of id {product_id} does not exists! Please provice a valid id",
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has this item on the wishlist",
        )


@wishlist_router.get(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=WishlistItemDetailed
)
async def get_user_withlist_item(product_id: str, user: User = Depends(current_active_user)):
    try:
        item = await WishlistController().get_item_from_user_wishlist(product_id, str(user.id))
        return Response(content=item.json(), media_type="application/json")
    except AttributeError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not have this item on the wishlist",
        )


@wishlist_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=WishlistDetailed
)
async def get_user_withlist(user: User = Depends(current_active_user)):
    try:
        items = await WishlistController().get_entire_user_wishlist(str(user.id))
        return Response(content=json.dumps(items), media_type="application/json")
    except Exception as e:
        raise e


def set_wishlist_router(app):
    app.include_router(wishlist_router)
