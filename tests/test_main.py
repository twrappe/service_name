from fastapi.testclient import TestClient
from src.package.main import app

client = TestClient(app)

def test_root():
    """Test the root endpoint returns a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the" in response.json().get("message", "")

def test_health():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "__SERVICE_NAME__" in data["service"]

def test_create_item():
    """Test the POST /items endpoint with example data."""
    payload = {"name": "test-item", "value": 42}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == "test-item"
    assert data["item"]["value"] == 42
    assert data["message"] == "Item received"
