import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from fastapi.testclient import TestClient
from src.api.main import app


client = TestClient(app)


def test_get_requests():
    """GET /requests/ — успешный запрос."""
    response = client.get("/requests/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_ticket():
    """GET /requests/999 — отсутствующий ресурс."""
    response = client.get("/requests/999")
    assert response.status_code == 404


def test_create_invalid_ticket():
    """POST /requests/ с пустым title — ошибочный ввод."""
    response = client.post("/requests/", json={
        "title": "",
        "category_id": 1,
        "author_id": 1
    })
    assert response.status_code == 422