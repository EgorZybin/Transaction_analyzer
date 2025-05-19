from src.services.stats import compute_stats
from types import SimpleNamespace
from datetime import datetime

def make_tx(amount, category, date_str):
    return SimpleNamespace(
        amount=amount,
        category=category,
        timestamp=datetime.fromisoformat(date_str)
    )

def test_compute_stats():
    """Проверяет корректность расчёта общей суммы, разбивки по категориям и среднего по дням."""
    txs = [
        make_tx(-100.0, "Food", "2024-11-01T10:00:00"),
        make_tx(-200.0, "Transport", "2024-11-01T11:00:00"),
        make_tx(-300.0, "Food", "2024-11-02T10:00:00")
    ]
    result = compute_stats(txs)
    assert result["total_spent"] == 600.0
    assert result["by_category"] == {"Food": 400.0, "Transport": 200.0}
    assert result["daily_average"] == 300.0