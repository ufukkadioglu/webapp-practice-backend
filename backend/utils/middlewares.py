from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from enum import Enum
from fastapi.responses import PlainTextResponse


class ApiStatus(Enum):
    Healthy = 1
    UnderMaintenance = 0
    Unhealthy = -1


STATUS_VALUES = [m.value for m in ApiStatus]


class StatusManager(BaseHTTPMiddleware):
    API_INSTANCE_STATUS = ApiStatus.Healthy.value

    async def dispatch(self, request: Request, call_next):
        print("StatusManager")

        if StatusManager.API_INSTANCE_STATUS != ApiStatus.Healthy.value and request.scope["path"] != '/api_status/update':
            response = PlainTextResponse(content="Api under maintenance")
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
            return response

        return await call_next(request)


class RequestAnalyzer(BaseHTTPMiddleware):
    ACTIVE_REQUEST_COUNT = 0

    @staticmethod
    def get_active_request_count():
        return RequestAnalyzer.ACTIVE_REQUEST_COUNT

    async def dispatch(self, request: Request, call_next):
        print("RequestAnalyzer")
        if request.scope["path"] != '/active_request_count':
            RequestAnalyzer.ACTIVE_REQUEST_COUNT = RequestAnalyzer.ACTIVE_REQUEST_COUNT + 1

        response = await call_next(request)

        if request.scope["path"] != '/active_request_count':
            RequestAnalyzer.ACTIVE_REQUEST_COUNT = RequestAnalyzer.ACTIVE_REQUEST_COUNT - 1
        return response
