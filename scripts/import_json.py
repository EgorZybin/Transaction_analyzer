import json
from src.database import SessionLocal, init_db
from src.schemas import TransactionIn
from src.crud import add_transaction
from src.services.categorizer import categorize
from datetime import datetime

init_db()
db = SessionLocal()

with open("data/transactions.json", "r", encoding="utf-8") as f:
    transactions = json.load(f)

for tx in transactions:
    if "category" not in tx or not tx["category"]:
        tx["category"] = categorize(tx.get("description", ""))
    tx["timestamp"] = datetime.fromisoformat(tx["timestamp"])
    add_transaction(db, TransactionIn(**tx))

print("Imported", len(transactions), "transactions")