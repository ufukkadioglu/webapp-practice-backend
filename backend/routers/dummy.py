import time
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

router = APIRouter()


class User(BaseModel):
    name: str
    is_awesome: bool


users: list[User] = []


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/say_hello")
def say_hello(name: str = None):
    if not name and users:
        name = users[-1].name
    return PlainTextResponse(f"Hello {name}")


@router.put("/users/new")
def update_user(user: User):
    users.append(user)
    return {"name": user.name, "is_awesome": user.is_awesome}
