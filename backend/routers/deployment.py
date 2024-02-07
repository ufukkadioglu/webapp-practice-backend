from fastapi import APIRouter
from utils.middlewares import RequestAnalyzer, StatusManager, STATUS_VALUES

router = APIRouter()


@router.get("/active_request_count")
def get_active_request_count():
    return RequestAnalyzer.ACTIVE_REQUEST_COUNT


@router.get("/api_status")
def get_api_status():
    return StatusManager.API_INSTANCE_STATUS


@router.post("/api_status/update")
def update_api_status(api_status: int):
    if api_status not in STATUS_VALUES:
        return "Invalid status"

    StatusManager.API_INSTANCE_STATUS = api_status
    return f"New status: {StatusManager.API_INSTANCE_STATUS}"
