from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from src import database, crud, schemas, models
from src.services import categorizer, limiter, stats

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions/")
def import_transaction(tx: schemas.TransactionIn, db: Session = Depends(get_db)):
    """Импортирует транзакцию в базу данных.

    Если категория не указана, она будет определена автоматически по описанию.

    Args:
        tx (TransactionIn): Входные данные транзакции.

    Returns:
        dict: Статус выполнения.
    """
    if not tx.category and tx.description:
        tx.category = categorizer.categorize(tx.description)
    crud.add_transaction(db, tx)
    return {"status": "ok"}

@router.get("/users/{user_id}/stats", response_model=schemas.StatsOut)
def get_stats(user_id: int, from_: str, to: str, db: Session = Depends(get_db)):
    """Возвращает статистику расходов пользователя за указанный период.

    Статистика включает:
    - Общую сумму расходов
    - Расходы по категориям
    - Среднее дневное значение

    Также логирует предупреждение, если лимиты трат превышены.

    Args:
        user_id (int): ID пользователя.
        from_ (str): Начальная дата периода (в формате YYYY-MM-DD).
        to (str): Конечная дата периода.

    Returns:
        StatsOut: Статистика по транзакциям.
    """
    start = datetime.fromisoformat(from_)
    end = datetime.fromisoformat(to)
    txs = db.query(models.Transaction).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.timestamp.between(start, end)
    ).all()
    limiter.check_limits(txs)
    return stats.compute_stats(txs)