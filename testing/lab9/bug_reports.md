\# Отчёт о дефектах



&#x20;  BUG-01 — FOREIGN KEY constraint failed при создании заявки



&#x20;  Среда и версия:

\- Локально: http://127.0.0.1:8000

\- Удалённо: https://strizhov-danila-isip-407-requestsystem.onrender.com

\- Коммит: 35670eb

\- Инструмент: Swagger UI



&#x20; Шаги воспроизведения:

1\. Открыть Swagger UI.

2\. Выбрать POST /requests/.

3\. Ввести тело:

{"title": "Тест бага", "category\_id": 1, "author\_id": 999}

4\. Нажать Execute.



&#x20;  Ожидаемый результат:

HTTP 422 (Unprocessable Entity) с сообщением о несуществующем авторе.



&#x20;  Фактический результат:

HTTP 500 Internal Server Error.

{"detail": "Внутренняя ошибка сервера"}



&#x20;  Важность: High — некорректная обработка ошибок.



&#x20;  Доказательство: tc14\_bad\_author.png.



&#x20;  Статус: Новый.



&#x20;  Причина (из логов uvicorn):

sqlite3.IntegrityError: FOREIGN KEY constraint failed

SQLite отклоняет вставку из-за внешнего ключа. В TicketService.create\_ticket нет проверки существования автора.



&#x20;  Рекомендация:

Добавить проверку author\_id через UserRepository.get\_by\_id перед созданием заявки.



\---



&#x20;  BUG-02 — POST /requests/ возвращает 500 (database is locked)



&#x20;  Среда и версия:

\- Локально: http://127.0.0.1:8000

\- Удалённо: https://strizhov-danila-isip-407-requestsystem.onrender.com

\- Коммит: 35670eb

\- Инструмент: Swagger UI



&#x20;  Шаги воспроизведения:

1\. Открыть Swagger UI.

2\. Выбрать POST /requests/.

3\. Ввести тело:

{"title": "Тестовая заявка", "description": "Проверка API", "category\_id": 1, "author\_id": 1}

4\. Нажать Execute.



&#x20;  Ожидаемый результат:

HTTP 201 Created + созданная заявка.



&#x20;  Фактический результат:

HTTP 500 Internal Server Error.

{"detail": "Внутренняя ошибка сервера"}



&#x20;  Важность: Critical — невозможно создать заявку.



&#x20;  Доказательство: tc01\_post\_fail.png.



&#x20;  Статус: Новый.



&#x20;  Причина (из логов uvicorn):

sqlite3.OperationalError: database is locked

SQLite не может записать в БД — она заблокирована другим процессом (DB Browser).



&#x20;  Рекомендация:

1\. Убедиться, что БД не открыта в DB Browser.

2\. Использовать timeout при подключении к SQLite.

3\. Перейти на PostgreSQL для параллельной работы.



\---



&#x20;  Дефектов больше не обнаружено



Остальные 24 тест-кейса прошли успешно (PASS). Один тест (TC-04) отмечен BLOCKED — поиск в API не реализован.

