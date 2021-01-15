from starlette.testclient import TestClient
from app.core.config import settings
from app.main import app
import requests


client = TestClient(app)

def test_get_hello():
    response = client.get(f"{settings.API_V1}/user")
    assert response.status_code == 200