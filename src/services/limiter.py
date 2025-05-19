from collections import defaultdict

DAILY_LIMIT = 1000
WEEKLY_LIMIT = 5000

def check_limits(transactions):
    """Проверяет, превышены ли дневной или недельный лимиты расходов.

    Выводит предупреждение в консоль, если лимиты превышены.

    Args:
        transactions (list): Список транзакций.
    """
    by_day = defaultdict(float)
    for t in transactions:
        if t.amount < 0:
            by_day[t.timestamp.date()] += -t.amount
    for day, total in by_day.items():
        if total > DAILY_LIMIT:
            print(f"Over daily limit {day}: {total}")
    week_total = sum(v for v in by_day.values())
    if week_total > WEEKLY_LIMIT:
        print(f"Over weekly limit: {week_total}")