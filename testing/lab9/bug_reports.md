&#x20;  Отчёт о дефектах



&#x20;  BUG-01 — Некорректная обработка несуществующего автора



Среда и версия:

\- Локально: http://127.0.0.1:8000

\- Удалённо: https://strizhov-danila-isip-407-requestsystem.onrender.com

\- Коммит: 35670eb

\- Инструмент: Swagger UI



Шаги воспроизведения:

1\. Открыть Swagger UI.

2\. Выбрать POST /requests/.

3\. Ввести тело:

&#x20;  ```json

&#x20;  {"title": "Тест бага", "category\_id": 1, "author\_id": 999}

