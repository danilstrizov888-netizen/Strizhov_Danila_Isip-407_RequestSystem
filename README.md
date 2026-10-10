Система учёта заявок (RequestSystem)

Учебный проект по дисциплине «Технологии разработки программного обеспечения».

---

   О проекте

Система предназначена для регистрации, обработки и контроля заявок внутри организации.
Позволяет фиксировать обращения, назначать исполнителей, отслеживать статусы
и хранить историю работы по каждой заявке.

Добавлена ветка develop — для разработки новых функций.

---

   Автор

Студент: Стрижов Данила

Группа: Исип-407

Дисциплина: Технологии разработки программного обеспечения

---

   Как запустить

1. Установи Python 3.12+.

2. Клонируй репозиторий:

   git clone https://github.com/danilstrizov888-netizen/Strizhov_Danila_Isip-407_RequestSystem.git

   cd Strizhov_Danila_Isip-407_RequestSystem

3. Запусти приложение:

   python -m src.main

4. Выбери действие в меню.

---

   Функционал

- Просмотр всех заявок

- Создание заявки

- Открытие заявки по ID

- Поиск по названию и описанию

- Фильтрация по статусу

- Изменение статуса заявки

- Назначение исполнителя

- Редактирование заявки

- Удаление с подтверждением

- Просмотр пользователей

---

   REST API

Запуск локально:

   uvicorn src.api.main:app --reload

Адрес локально: http://127.0.0.1:8000

Документация (Swagger): http://127.0.0.1:8000/docs

---

   Удалённый деплой

Приложение развёрнуто на Render.com:

Адрес: https://strizhov-danila-isip-407-requestsystem.onrender.com

Ссылки:

- Swagger: https://strizhov-danila-isip-407-requestsystem.onrender.com/docs

- Health: https://strizhov-danila-isip-407-requestsystem.onrender.com/health

- Requests: https://strizhov-danila-isip-407-requestsystem.onrender.com/requests/

---

   Endpoints

| Метод | Путь | Назначение |

|-------|------|-----------|

| GET | /requests/ | Список заявок |

| GET | /requests/{id} | Одна заявка |

| POST | /requests/ | Создать заявку |

| PATCH | /requests/{id} | Обновить заявку |

| DELETE | /requests/{id} | Удалить заявку |

| GET | /users/ | Пользователи |

| GET | /statuses/ | Статусы |

| GET | /categories/ | Категории |

| GET | /health | Проверка работоспособности |

Пример запроса:

   curl -X GET "http://127.0.0.1:8000/requests/"

---

   Docker

Сборка образа:

   docker build -t request-system .

Запуск контейнера:

   docker run -d -p 8000:8000 --name request-api request-system

Проверка:

   docker ps

   curl http://127.0.0.1:8000/health

---

   Деплой на Render.com

1. Зарегистрируйся на https://render.com.

2. Подключи GitHub-репозиторий.

3. Создай Web Service:

   - Language: Docker

   - Branch: main

   - Region: Frankfurt

   - Instance Type: Free

4. Render автоматически соберёт Docker-образ и запустит контейнер.

5. После деплоя приложение доступно по ссылке.

---

   Тестирование

---

   Локальное тестирование

Запуск тестов:

   cd testing/lab9

   cat test_plan.md

   cat test_cases.md

   cat bug_reports.md

---

   Результаты

| Категория | PASS | FAIL | BLOCKED |
|-----------|:----:|:----:|:-------:|
| Позитивные | 9 | 1 | 0 |
| Негативные | 3 | 1 | 0 |
| Граничные | 4 | 0 | 0 |
| Роли | 2 | 0 | 0 |
| Интеграционные | 2 | 0 | 0 |
| API | 4 | 0 | 0 |
| Итого | 24 | 2 | 1 |

---

   Найденные дефекты

| ID | Название | Важность |
|----|----------|:--------:|
| BUG-01 | FOREIGN KEY constraint failed | High |
| BUG-02 | Database is locked | Critical |

---

   Переменные окружения

Файл `.env.example`:

   APP_PORT=8000

   DB_PATH=docs/db/requests.db

Для локального запуска скопируй `.env.example` в `.env`.

Файл `.env` добавлен в `.gitignore` — секреты не попадают в Git.

---

   Структура проекта

RequestSystem/

├── docs/

│   ├── TZ.md

│   ├── ai_log.md

│   ├── ai_screenshots/

│   ├── use_case.png

│   ├── architecture/

│   │   ├── architecture.md

│   │   ├── architecture.png

│   │   └── components.png

│   ├── ui/

│   │   ├── README.md

│   │   ├── login.png

│   │   ├── tickets.png

│   │   ├── create_ticket.png

│   │   ├── ticket_card.png

│   │   └── edit_ticket.png

│   ├── api_screenshots/

│   │   ├── swagger_main.png

│   │   ├── get_requests.png

│   │   ├── post_request.png

│   │   ├── patch_request.png

│   │   ├── delete_request.png

│   │   ├── get_users.png

│   │   ├── get_statuses.png

│   │   ├── get_categories.png

│   │   ├── error_404.png

│   │   ├── health_local.png

│   │   ├── health_remote.png

│   │   ├── docker_swagger.png

│   │   ├── docker_requests.png

│   │   ├── docker_ps.png

│   │   ├── render_logs.png

│   │   ├── swagger_remote.png

│   │   ├── requests_remote.png

│   │   └── curl_commands.md

│   └── db/

│       ├── schema.sql

│       ├── seed.sql

│       ├── queries.sql

│       ├── requests.db

│       ├── er_diagram.png

│       └── screenshots/

├── src/

│   ├── __init__.py

│   ├── main.py

│   ├── models/

│   │   ├── __init__.py

│   │   ├── ticket.py

│   │   └── user.py

│   ├── repository/

│   │   ├── __init__.py

│   │   ├── ticket_repository.py

│   │   └── user_repository.py

│   ├── service/

│   │   ├── __init__.py

│   │   └── ticket_service.py

│   ├── api/

│   │   ├── __init__.py

│   │   ├── main.py

│   │   ├── schemas.py

│   │   └── routes/

│   │       ├── __init__.py

│   │       ├── requests.py

│   │       ├── users.py

│   │       ├── statuses.py

│   │       └── categories.py

│   └── presentation/

│       └── __init__.py

├── testing/

│   └── lab9/

│       ├── test_plan.md

│       ├── test_cases.md

│       ├── bug_reports.md

│       ├── api_collection.md

│       └── *.png (скриншоты)

├── tests/

├── Dockerfile

├── .dockerignore

├── .env.example

├── requirements.txt

└── README.md

---

   Документация

[Техническое задание](docs/TZ.md)

[AI-журнал](docs/ai_log.md)

[Диаграмма Use Case](docs/use_case.png)

[Архитектура](docs/architecture/architecture.md)

[Прототип интерфейса](docs/ui/README.md)

[База данных](docs/db/schema.sql)

[REST API — примеры запросов](docs/api_screenshots/curl_commands.md)

[Тест-план](testing/lab9/test_plan.md)

[Тест-кейсы](testing/lab9/test_cases.md)

[Отчёт о дефектах](testing/lab9/bug_reports.md)

---

   Технологии

Python 3.12+

SQLite (БД)

FastAPI + Uvicorn (REST API)

Docker (контейнеризация)

Render.com (деплой)

Git / GitHub

draw.io (diagrams.net) — для диаграмм

PlantUML — для архитектурных диаграмм

Markdown — для документации

---

   Статус проекта

✅ Лабораторная работа №1 — завершена.

✅ Лабораторная работа №2 — завершена.

✅ Лабораторная работа №3 — завершена.

✅ Лабораторная работа №4 — завершена.

✅ Лабораторная работа №5 — завершена.

✅ Лабораторная работа №6 — завершена.

✅ Лабораторная работа №7 — завершена.

✅ Лабораторная работа №8 — завершена.

✅ Лабораторная работа №9 — завершена.

⬜ Лабораторная работа №10 — выполняется.

⬜ Видео — выполняется.