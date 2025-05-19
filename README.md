# Transaction Analyzer

Мини-сервис для анализа пользовательских транзакций.  
Позволяет импортировать данные, автоматически категоризировать расходы, отслеживать превышение лимитов и получать статистику через REST API.

---

## Функциональность

- Импорт транзакций из JSON-файла
- Автоматическая категоризация по описанию
- Проверка превышения дневных/недельных лимитов
- Статистика трат по категориям и дням
- REST API с двумя эндпоинтами
- SQLite в качестве базы данных
- Полное покрытие тестами бизнес-логики и API

---

## Запуск
 
Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск приложения:

```bash
make run
```

Импорт транзакций:

```bash
make import
```

[http://127.0.0.1:8000/docs] — интерактивная Swagger-документация

---

## Пример запроса

```bash
curl "http://127.0.0.1:8000/users/1/stats?from_=2024-11-01&to=2024-11-03"
```

Ответ:
```json
{
  "total_spent": 1170.75,
  "by_category": {
    "Food": 450.75,
    "Transport": 120.0,
    "Entertainment": 600.0
  },
  "daily_average": 1170.75
}
```

---

## Тестирование

В проекте есть тесты:
- `categorizer` — проверка категоризации по ключевым словам
- `stats` — расчёт статистики
- `limiter` — проверка лимитов с логированием
- `routes` — полный путь: импорт + API

Запуск тестов:

```bash
make test
```

---

## Makefile команды

- `make run`      Запускает FastAPI приложение                                   
- `make import`   Импортирует транзакции из `scripts/import_json.py`             
- `make test`     Запускает все тесты                                            
- `make db`       Открывает SQLite-базу в консоли (если установлен `sqlite3`)    

---

## Структура проекта

```
transaction_analyzer/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── api/routes.py
│   └── services/
│       ├── categorizer.py
│       ├── limiter.py
│       └── stats.py
├── scripts/
│   └── import_json.py
├── tests/
│   ├── test_categorizer.py
│   ├── test_limiter.py
│   ├── test_routes.py
│   └── test_stats.py
├── data/transactions.json
├── requirements.txt
├── Makefile
└── README.md
```

---

## Автор

Егор Зыбин: Github[https://github.com/EgorZybin] Telegram[https://t.me/raizzep]
