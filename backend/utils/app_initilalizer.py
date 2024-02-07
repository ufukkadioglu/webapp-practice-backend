from fastapi import FastAPI
from utils.my_logger import create_loggers
from utils.singleton_instances import set_instances


def initialize_app():
    app = FastAPI()

    logger = create_loggers()

    logger.info("logger created")

    logger.info("Setting singleton instances")

    set_instances(app, logger)

    logger.info("Including routers")

    include_all_routers(app)

    logger.info("App ready!")

    return app


def include_all_routers(app):
    from routers import dummy

    app.include_router(dummy.router)
