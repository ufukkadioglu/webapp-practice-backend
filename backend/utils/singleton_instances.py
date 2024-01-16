from utils.singleton_classes import App, Logger

app: App
logger: Logger


def initialize_instances(app_instance, logger_instance):
    global app, logger
    app = app_instance
    logger = logger_instance
