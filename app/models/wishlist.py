from sqlalchemy import Column, Integer, String,  ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from models import User

Base: DeclarativeMeta = declarative_base()


class Wishlist(Base):
    __tablename__ = 'wishlist'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, index=True)
    owner_id = Column(UUID, ForeignKey(User.id))

    owner = relationship(User, backref="wishlist")

    __table_args__ = (UniqueConstraint('product_id', 'owner_id'),)
