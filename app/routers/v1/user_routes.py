from fastapi import APIRouter
from app.core.config import settings


router = APIRouter(
    prefix = '/user'
)


@router.get('')
async def hello_world():
    return {'message': 'Teste git PC2'}