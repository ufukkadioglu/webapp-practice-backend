import uvicorn
from utils.app_initilalizer import initialize_app
from utils.middlewares import RequestAnalyzer, StatusManager

print("Initializing app from main.py")
app = initialize_app()

app.add_middleware(RequestAnalyzer)
app.add_middleware(StatusManager)

if __name__ == "__main__":
    from utils.singleton_instances import logger

    logger.info("Starting app from main.py")
    uvicorn.run(app, port=5000, log_level="info")
    logger.info("App stopped")
