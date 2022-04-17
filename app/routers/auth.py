import os
from typing import List

from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from controllers.user import get_user_manager
from schemas.user import User, UserCreate, UserUpdate, UserDB

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET = os.environ.get("JWT_SECRET")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=86400)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


def set_fastapi_users_router(
    router: APIRouter,
    prefix: str,
    tags: List[str]
) -> APIRouter:
    router.prefix = prefix
    router.tags = tags
    return router


fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_active_user = fastapi_users.current_user(active=True)

auth_router = set_fastapi_users_router(
    fastapi_users.get_auth_router(auth_backend),
    "/auth/jwt",
    ["auth"]
)

register_router = set_fastapi_users_router(
    fastapi_users.get_register_router(),
    "/auth",
    ["auth"]
)

reset_password_router = set_fastapi_users_router(
    fastapi_users.get_reset_password_router(),
    "/auth",
    ["auth"]
)

verify_router = set_fastapi_users_router(
    fastapi_users.get_verify_router(),
    "/auth",
    ["auth"]
)

users_router = set_fastapi_users_router(
    fastapi_users.get_users_router(),
    "/users",
    ["users"]
)

routers = [
    auth_router,
    register_router,
    reset_password_router,
    verify_router,
    users_router
]


def set_auth_routers(app):
    for router in routers:
        app.include_router(
            router,
            prefix=router.prefix,
            tags=router.tags
        )
