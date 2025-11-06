
Реализовано на **FastAPI**, **SQLAlchemy (async)**, **PostgreSQL**, **Alembic** и **Docker**.

---
### Запуск проекта через Docker Compose
```bash

docker compose up --build 
```
---
### Применить миграции
```bash

docker compose exec app alembic upgrade head 
```

---
### API:
#### 1. POST /v1/incident/ - создать новый инцидент
#### 2. POST /v1/incident/ - получить все инциденты по фильтру status
#### 3. PATCH /v1/incident/{incident_id} - обновить инцидент по id 

---
### Документация досутпна по http://localhost:8000/docs 


