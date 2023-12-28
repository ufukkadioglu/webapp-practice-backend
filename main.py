from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    is_awesome: bool


users: list[User] = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/say_hello")
def read_item(name: str = None):
    if not name and users:
        name = users[-1].name
    return f"Hello {name}"


@app.put("/users/new")
def update_user(user: User):
    users.append(user)
    return {"name": user.name, "is_awesome": user.is_awesome}
