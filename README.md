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

Запуск:

   uvicorn src.api.main:app --reload

Адрес: http://127.0.0.1:8000

Документация (Swagger): http://127.0.0.1:8000/docs

Endpoints:

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

Пример запроса:

   curl -X GET "http://127.0.0.1:8000/requests/"

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

│   │   ├── get_requests_filter.png

│   │   ├── post_request.png

│   │   ├── get_request.png

│   │   ├── patch_request.png

│   │   ├── delete_request.png

│   │   ├── get_users.png

│   │   ├── get_statuses.png

│   │   ├── get_categories.png

│   │   ├── error_404.png

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

├── tests/

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

---

   Технологии

Python 3.12+

SQLite (БД)

FastAPI + Uvicorn (REST API)

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

⬜ Лабораторная работа №8 — выполняется.

⬜ Лабораторная работа №9 — выполняется.

⬜ Лабораторная работа №10 — выполняется.
