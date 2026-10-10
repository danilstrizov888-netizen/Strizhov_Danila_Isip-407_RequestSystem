&#x20;  Автоматические тесты (лабораторная №10)



&#x20;  Установка зависимостей



pip install pytest httpx fastapi



\---



&#x20;  Запуск тестов



Из корня проекта:



pytest testing/lab10/ -v



Или с сохранением лога:



pytest testing/lab10/ -v > testing/lab10/test\_run.txt



\---



&#x20;  Структура тестов



| Файл | Что проверяет |

|------|---------------|

| test\_api.py | API-запросы (GET, POST, 404, 422) |

| test\_business.py | Бизнес-логика (TicketService) |

| test\_regression.py | Регрессия для BUG-01 и BUG-02 |



\---



&#x20;  Результат



8 тестов, все PASSED.



\---



&#x20;  Требования



\- Python 3.12+

\- pytest

\- httpx

\- fastapi

