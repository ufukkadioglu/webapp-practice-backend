import uvicorn

from utils.app_initilalizer import initialize_app

if __name__ == "__main__":
    print("Starting app from main.py")
    app = initialize_app()
    uvicorn.run(app, port=5000, log_level="info")
    print("App stopped")
