from fastapi import FastAPI
from routers import dummy


def initialize_app():
    app = FastAPI()
    include_all_routers(app)
    return app


def include_all_routers(app):
    app.include_router(dummy.router)
