import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>Schizo Bots</title>" in response.text
    assert '<button id="pause-button" class="pause-button">Pause</button>' in response.text
    assert '<button id="new-chat-button" class="new-chat-button">New Chat</button>' in response.text

def test_new_chat():
    # Ensure the chat is not paused before starting a new chat
    client.post("/pause")
    
    response = client.post("/new-chat")
    assert response.status_code == 200
    assert response.json() == {"status": "new chat started"}

def test_pause():
    # Check initial pause state
    response = client.post("/pause")
    assert response.status_code == 200
    assert response.json()["paused"] is True

    # Toggle pause state back to False
    response = client.post("/pause")
    assert response.status_code == 200
    assert response.json()["paused"] is False