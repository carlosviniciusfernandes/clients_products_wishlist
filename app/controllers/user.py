import os
from typing import Optional, Union, Dict, Any

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, InvalidPasswordException
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import AsyncSession

from database import async_session_maker
from schemas.user import UserCreate, UserDB
from models.user import User as UserTable

SECRET = os.environ.get("JWT_SECRET")


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def validate_password(
        self, password: str, user: Union[UserCreate, UserDB]
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

    async def on_after_register(
        self, user: UserDB, request: Optional[Request] = None
    ):
        print(f"User {user.id} has registered.")

    async def on_after_update(
        self, user: UserDB, update_dict: Dict[str, Any], request: Optional[Request] = None
    ):
        print(f"User {user.id} has been updated with {update_dict}.")

    async def on_after_request_verify(
        self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def on_after_verify(
        self, user: UserDB, request: Optional[Request] = None
    ):
        print(f"User {user.id} has been verified")

    async def on_after_forgot_password(
        self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_reset_password(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has reset their password.")


async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(UserDB, session, UserTable)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
