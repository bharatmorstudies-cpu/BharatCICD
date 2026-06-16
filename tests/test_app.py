import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test that the home route returns a 200 status code and expected JSON."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World! Welcome to the Staging Environment."}
