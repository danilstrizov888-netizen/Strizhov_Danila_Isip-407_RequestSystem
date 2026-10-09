import os
from src.repository.ticket_repository import TicketRepository
from src.service.ticket_service import TicketService


def main():
    db_path = os.path.join("docs", "db", "requests.db")
    ticket_repo = TicketRepository(db_path)
    ticket_service = TicketService(ticket_repo)

    while True:
        print("\n=== Система учёта заявок ===")
        print("1. Показать все заявки")
        print("2. Создать заявку")
        print("3. Открыть заявку")
        print("4. Поиск заявок")
        print("5. Фильтр по статусу")
        print("6. Выход")
        choice = input("Выберите: ")

        if choice == "1":
            tickets = ticket_service.get_all()
            if not tickets:
                print("Заявок пока нет")
            for t in tickets:
                print(f"[{t.id}] {t.title} (status: {t.status_id})")

        elif choice == "2":
            title = input("Тема: ")
            description = input("Описание: ")
            try:
                ticket = ticket_service.create_ticket(title, description, 1, 1)
                print(f"Создана заявка №{ticket.id}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            try:
                ticket_id = int(input("ID заявки: "))
            except ValueError:
                print("Ошибка: ID должен быть числом")
                continue
            try:
                t = ticket_service.get_by_id(ticket_id)
                print(f"Заявка: {t.title}")
                print(f"Описание: {t.description}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            query = input("Поиск: ")
            try:
                tickets = ticket_service.search(query)
                if not tickets:
                    print("Ничего не найдено")
                for t in tickets:
                    print(f"[{t.id}] {t.title}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            print("Статусы: 1-Новая, 2-В работе, 3-Выполнена, 4-Закрыта")
            try:
                status_id = int(input("Статус: "))
            except ValueError:
                print("Ошибка: статус должен быть числом")
                continue
            tickets = ticket_service.filter_by_status(status_id)
            if not tickets:
                print("Заявок с таким статусом нет")
            for t in tickets:
                print(f"[{t.id}] {t.title} (status: {t.status_id})")

        elif choice == "6":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()