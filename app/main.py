from fastapi import FastAPI
from .routers.v1 import user_routes
from .core.config import settings


app = FastAPI()


app.include_router(user_routes.router, prefix=settings.API_V1)
