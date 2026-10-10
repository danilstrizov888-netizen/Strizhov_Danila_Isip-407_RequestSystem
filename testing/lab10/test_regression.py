import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from fastapi.testclient import TestClient
from src.api.main import app


client = TestClient(app)


def test_bug01_nonexistent_author():
    """BUG-01 fix: POST с author_id=999 → 422."""
    response = client.post("/requests/", json={
        "title": "Тест регрессии",
        "category_id": 1,
        "author_id": 999
    })
    assert response.status_code == 422


def test_bug02_database_lock():
    """BUG-02 fix: POST с корректными данными → 201."""
    response = client.post("/requests/", json={
        "title": "Тест регрессии 2",
        "category_id": 1,
        "author_id": 1
    })
    assert response.status_code == 201