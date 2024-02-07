import os
import logging
import yaml

LOGGER_NAME = "default_logger"


def create_loggers(default_path='configs/logging.yaml', env_key='FASTAPI_WEBAPP_LOG_CONFIG'):
    path = default_path
    value = os.getenv(env_key, None)

    if value:
        path = value

    if not os.path.exists(path):
        raise Exception("Failed to load logger")

    with open(path, 'rt') as f:
        config = yaml.safe_load(f.read())

    logging.config.dictConfig(config)
    default_logger = logging.getLogger(LOGGER_NAME)
    return default_logger
