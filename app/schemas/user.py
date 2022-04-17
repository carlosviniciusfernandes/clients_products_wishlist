from fastapi_users import models


class User(models.BaseUser):
    first_name: str
    last_name: str


class UserCreate(models.BaseUserCreate):
    first_name: str
    last_name: str


class UserUpdate(models.BaseUserUpdate):
    first_name: str
    last_name: str


class UserDB(User, models.BaseUserDB):
    first_name: str
    last_name: str
