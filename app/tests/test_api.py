from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Visit /static/index.html to use the web UI." in response.json()["message"]

def test_random_advice():
    response = client.get("/encouragement")
    assert response.status_code == 200
    assert "encouragement" in response.json()

def test_city_advice():
    response = client.get("/encouragement/new_york")
    assert response.status_code == 200
    assert "encouragement" in response.json()
