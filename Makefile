# Запускает FastAPI сервер на http://127.0.0.1:8000
run:
	uvicorn src.main:app --reload
# Импортирует фейковые транзакции из scripts/import_json.py в базу данных
import:
	python -m scripts.import_json
# Запускает все тесты с учётом импорта src как модуля
test:
	set PYTHONPATH=. && pytest tests
# Открывает SQLite-базу в интерактивном режиме (если установлен sqlite3)
db:
	sqlite3 db.sqlite