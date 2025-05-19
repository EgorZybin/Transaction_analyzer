from src.services.categorizer import categorize

def test_categorize_food():
    """Проверяет, что описания, связанные с едой, попадают в категорию 'Food'."""
    assert categorize("KFC lunch") == "Food"
    assert categorize("just FOOD") == "Food"

def test_categorize_transport():
    """Проверяет, что транспортные описания попадают в категорию 'Transport'."""
    assert categorize("bus ticket") == "Transport"
    assert categorize("TAXI ride") == "Transport"

def test_categorize_entertainment():
    """Проверяет, что развлекательные описания попадают в категорию 'Entertainment'."""
    assert categorize("Netflix monthly") == "Entertainment"
    assert categorize("movie night") == "Entertainment"

def test_categorize_utilities():
    """Проверяет, что коммунальные расходы попадают в категорию 'Utilities'."""
    assert categorize("Rent for April") == "Utilities"
    assert categorize("phone bill") == "Utilities"

def test_categorize_other():
    """Проверяет, что неизвестные описания попадают в категорию 'Other'."""
    assert categorize("random stuff") == "Other"