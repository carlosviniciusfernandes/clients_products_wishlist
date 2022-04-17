from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from auth import current_active_user
from controllers.wishlist import WishlistController
from schemas.user import User
from schemas.wishlist import WishlistItemCreate, WishlistItem, Wishlist

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
    wishlist_item = WishlistItemCreate(product_id=product_id, owner_id=str(user.id))
    try:
        return await WishlistController().add_item_to_wishlist(wishlist_item)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has this item on the wishlist",
        )


@wishlist_router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=WishlistItem
)
async def get_user_withlist_item(id: int, user: User = Depends(current_active_user)):
    try:
        return await WishlistController().get_item_from_wishlist(id, str(user.id))
    except AttributeError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not have this item on the wishlist",
        )


@wishlist_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Wishlist
)
async def get_user_withlist(user: User = Depends(current_active_user)):
    try:
        return await WishlistController().get_entire_wishlist(str(user.id))
    except Exception as e:
        raise e


def set_wishlist_router(app):
    app.include_router(wishlist_router)
