\# Примеры запросов к REST API



Базовый адрес: `http://127.0.0.1:8000`



\---



&#x20;  1. GET /requests/ — список заявок



curl -X GET "http://127.0.0.1:8000/requests/"



\---



&#x20;  2. GET /requests/?status\_id=1 — фильтр по статусу



curl -X GET "http://127.0.0.1:8000/requests/?status\_id=1"



\---



&#x20;  3. GET /requests/1 — одна заявка по ID



curl -X GET "http://127.0.0.1:8000/requests/1"



\---



&#x20;  4. POST /requests/ — создание заявки



curl -X POST "http://127.0.0.1:8000/requests/" \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"title": "Заявка через API", "description": "Создана через curl", "category\_id": 1, "author\_id": 1}'



\---



&#x20;  5. PATCH /requests/1 — обновление заявки



curl -X PATCH "http://127.0.0.1:8000/requests/1" \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"status\_id": 3}'



\---



&#x20;  6. DELETE /requests/21 — удаление заявки



curl -X DELETE "http://127.0.0.1:8000/requests/21"



\---



&#x20;  7. GET /users/ — список пользователей



curl -X GET "http://127.0.0.1:8000/users/"



\---



&#x20;  8. GET /statuses/ — справочник статусов



curl -X GET "http://127.0.0.1:8000/statuses/"



\---



&#x20;  9. GET /categories/ — справочник категорий



curl -X GET "http://127.0.0.1:8000/categories/"



\---



&#x20;  10. GET /requests/999 — ошибка 404



curl -X GET "http://127.0.0.1:8000/requests/999"

