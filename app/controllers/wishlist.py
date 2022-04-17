from sqlalchemy import select
from database import async_session_maker

from models.wishlist import Wishlist as WishlistModel
from schemas.wishlist import WishlistItem, WishlistItemCreate, Wishlist


class WishlistController():

    @staticmethod
    async def add_item_to_wishlist(wishlist_item: WishlistItemCreate) -> Wishlist:
        item = WishlistModel(**wishlist_item.dict())
        async with async_session_maker() as db_session:
            db_session.add(item)
            await db_session.commit()
            db_session.refresh(item)
        return item

    @staticmethod
    async def get_item_from_wishlist(id: int, owner_id: str) -> WishlistItem:
        async with async_session_maker() as db_session:
            statement = select(WishlistModel).filter_by(id=id, owner_id=owner_id)
            results = await db_session.execute(statement)
            item = results.first()
        return item.Wishlist

    @staticmethod
    async def get_entire_wishlist(owner_id: str) -> Wishlist:
        async with async_session_maker() as db_session:
            statement = select(WishlistModel).filter_by(owner_id=owner_id)
            results = await db_session.execute(statement)
            itens = results.all()
        return [item.Wishlist for item in itens] if itens else []
