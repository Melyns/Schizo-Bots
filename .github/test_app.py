import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_new_chat():
    response = client.post("/new-chat")
    assert response.status_code == 200
    assert response.json() == {"status": "new chat started"}

def test_pause():
    response = client.post("/pause")
    assert response.status_code == 200
    assert response.json()["paused"] is True

    response = client.post("/pause")
    assert response.status_code == 200
    assert response.json()["paused"] is False
