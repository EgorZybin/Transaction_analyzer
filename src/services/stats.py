from collections import defaultdict

def compute_stats(transactions: list) -> dict:
    """Вычисляет общую сумму расходов, статистику по категориям и среднюю дневную трату.

    Args:
        transactions (list): Список транзакций.

    Returns:
        dict: Словарь с ключами total_spent, by_category, daily_average.
    """
    total = sum(-t.amount for t in transactions if t.amount < 0)
    by_category = defaultdict(float)
    by_day = defaultdict(float)

    for t in transactions:
        if t.amount < 0:
            by_category[t.category] += -t.amount
            by_day[t.timestamp.date()] += -t.amount

    days = len(by_day) or 1
    return {
        "total_spent": round(total, 2),
        "by_category": {k: round(v, 2) for k, v in by_category.items()},
        "daily_average": round(total / days, 2)
    }