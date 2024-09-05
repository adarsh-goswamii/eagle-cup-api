from fastapi import APIRouter
from versions.v1 import auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix='/v1/auth', tags=["Auth"])