from sqlalchemy import select
from database import async_session_maker

from models.wishlist import Wishlist as WishlistModel
from schemas.wishlist import WishlistDetailed, WishlistItem, WishlistItemCreate, WishlistItemDetailed


class WishlistController:

    @staticmethod
    async def add_item_to_wishlist(wishlist_item: WishlistItemCreate) -> WishlistItem:
        item = WishlistModel(**wishlist_item.dict())
        async with async_session_maker() as db_session:
            db_session.add(item)
            await db_session.commit()
            db_session.refresh(item)
        return item

    @staticmethod
    async def get_item_from_user_wishlist(product_id: int, owner_id: str) -> WishlistItemDetailed:
        async with async_session_maker() as db_session:
            statement = select(WishlistModel).filter_by(product_id=product_id, owner_id=owner_id)
            results = await db_session.execute(statement)
            item = results.first()
        return WishlistItemDetailed(item.Wishlist)

    @staticmethod
    async def get_entire_user_wishlist(owner_id: str) -> WishlistDetailed:
        async with async_session_maker() as db_session:
            statement = select(WishlistModel).filter_by(owner_id=owner_id)
            results = await db_session.execute(statement)
            items = results.all()
            wishlist_items_detailed = [WishlistItemDetailed(item.Wishlist).dict() for item in items]
        return [item for item in wishlist_items_detailed if item]
