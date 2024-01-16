from fastapi import FastAPI
from utils.my_logger import create_loggers
from utils.singleton_instances import initialize_instances


def initialize_app():
    app = FastAPI()

    logger = create_loggers()

    initialize_instances(app, logger)

    include_all_routers(app)

    return app


def include_all_routers(app):
    from routers import dummy

    app.include_router(dummy.router)
