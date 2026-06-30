import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    # Match the exact JSON output returning from app.py
    assert b'{"message":"Hello, World! Welcome to the Staging Environment."}' in response.data
