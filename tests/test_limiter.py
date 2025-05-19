from src.services.limiter import check_limits
from types import SimpleNamespace
from datetime import datetime

def make_tx(amount, date_str):
    return SimpleNamespace(
        amount=amount,
        timestamp=datetime.fromisoformat(date_str)
    )

def test_check_limits(capsys):
    """Проверяет, что превышение лимитов выводится в консоль."""
    txs = [
        make_tx(-1100, "2024-11-01T10:00:00"),
        make_tx(-4000, "2024-11-02T12:00:00"),
    ]
    check_limits(txs)
    captured = capsys.readouterr().out
    assert "Over daily limit" in captured
    assert "Over weekly limit" in captured