from sqlalchemy.orm import Session
from src import models, schemas

def add_transaction(db: Session, tx: schemas.TransactionIn):
    """Добавляет транзакцию в базу данных.

    Args:
        db (Session): Сессия SQLAlchemy.
        tx (TransactionIn): Входные данные транзакции.
    """
    db_tx = models.Transaction(**tx.model_dump(exclude_unset=True))
    db.add(db_tx)
    db.commit()