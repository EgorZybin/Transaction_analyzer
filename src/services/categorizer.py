def categorize(description: str) -> str:
    """Определяет категорию транзакции по описанию.

    Args:
        description (str): Описание транзакции.

    Returns:
        str: Название категории (Food, Transport, Entertainment, Utilities, Other).
    """
    mapping = {
        'food': 'Food', 'kfc': 'Food',
        'taxi': 'Transport', 'bus': 'Transport',
        'movie': 'Entertainment', 'netflix': 'Entertainment',
        'rent': 'Utilities', 'phone': 'Utilities'
    }
    d = description.lower()
    for k, v in mapping.items():
        if k in d:
            return v
    return 'Other'