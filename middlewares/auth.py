from starlette.middleware.base import BaseHTTPMiddleware
from controllers import TokenJWT
import requests
import time

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: requests, call_next):
        TokenJWT.getToken()
        response = await call_next(request)
        return response
