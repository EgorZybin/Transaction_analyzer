from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    id: str
    user_id: int
    amount: float
    currency: str
    category: str | None = None
    timestamp: datetime
    description: str | None = None

class StatsOut(BaseModel):
    total_spent: float
    by_category: dict[str, float]
    daily_average: float
