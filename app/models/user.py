from sqlalchemy import Boolean, Column, String

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class User(Base, SQLAlchemyBaseUserTable):

    first_name = Column(String)
    last_name = Column(String)
    is_verified = Column(Boolean, default=True, nullable=False)  # For project simplicity defaults to True
