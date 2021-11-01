from fastapi import APIRouter

from app.api.api_v1.endpoints import predictions
from app.api.api_v1.endpoints import authentication

api_router = APIRouter()
api_router.include_router(predictions.router)
api_router.include_router(authentication.router)