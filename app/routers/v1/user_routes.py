from fastapi import APIRouter
from app.core.config import settings


router = APIRouter(
    prefix = '/user'
)


@router.get('')
async def hello_world():
    return {'message': settings.API_V1}#'new hello world'}