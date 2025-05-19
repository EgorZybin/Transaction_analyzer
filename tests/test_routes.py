from fastapi.testclient import TestClient
from src.main import app
from src.database import init_db
import uuid

client = TestClient(app)

def setup_module(module):
    """Создаёт структуру БД перед запуском тестов."""
    init_db()

def test_import_and_get_stats():
    """Проверяет, что можно импортировать транзакцию и получить по ней корректную статистику через API."""
    tx_id = str(uuid.uuid4())

    tx = {
        "id": tx_id,
        "user_id": 99,
        "amount": -500.0,
        "currency": "RUB",
        "timestamp": "2024-11-01T12:00:00",
        "description": "KFC lunch"
    }
    r = client.post("/transactions/", json=tx)
    assert r.status_code == 200

    r = client.get("/users/99/stats?from_=2024-11-01&to=2024-11-02")
    assert r.status_code == 200
    data = r.json()
    assert data["total_spent"] == 500.0
    assert data["by_category"]["Food"] == 500.0
    assert data["daily_average"] == 500.0