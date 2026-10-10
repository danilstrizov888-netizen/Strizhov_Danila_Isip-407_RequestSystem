import os
from src.repository.ticket_repository import TicketRepository
from src.repository.user_repository import UserRepository
from src.service.ticket_service import TicketService


def main():
    db_path = os.path.join("docs", "db", "requests.db")
    ticket_repo = TicketRepository(db_path)
    user_repo = UserRepository(db_path)
    ticket_service = TicketService(ticket_repo)

    while True:
        print("\n=== Система учёта заявок ===")
        print("1. Показать все заявки")
        print("2. Создать заявку")
        print("3. Открыть заявку")
        print("4. Поиск заявок")
        print("5. Фильтр по статусу")
        print("6. Изменить статус заявки")
        print("7. Назначить исполнителя")
        print("8. Редактировать заявку")
        print("9. Удалить заявку")
        print("10. Показать пользователей")
        print("11. Выход")
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
                print(f"Заявка №{t.id}: {t.title}")
                print(f"Описание: {t.description}")
                print(f"Статус: {t.status_id}")
                print(f"Исполнитель: {t.assignee_id}")
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
            try:
                ticket_id = int(input("ID заявки: "))
                print("Статусы: 1-Новая, 2-В работе, 3-Выполнена, 4-Закрыта")
                status_id = int(input("Новый статус: "))
                ticket_service.change_status(ticket_id, status_id)
                print(f"Статус заявки №{ticket_id} изменён на {status_id}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "7":
            print("\n--- Доступные исполнители ---")
            executors = user_repo.get_executors()
            for u in executors:
                print(f"[{u.id}] {u.full_name} ({u.login})")
            try:
                ticket_id = int(input("ID заявки: "))
                assignee_id = int(input("ID исполнителя: "))
                ticket_service.assign_executor(ticket_id, assignee_id)
                print(f"Исполнитель назначен на заявку №{ticket_id}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "8":
            try:
                ticket_id = int(input("ID заявки: "))
                new_title = input("Новая тема: ")
                new_description = input("Новое описание: ")
                ticket_service.update_ticket(ticket_id, new_title, new_description)
                print(f"Заявка №{ticket_id} обновлена")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "9":
            try:
                ticket_id = int(input("ID заявки: "))
                confirm = input(f"Удалить заявку №{ticket_id}? (y/n): ")
                if confirm.lower() == "y":
                    ticket_service.delete_ticket(ticket_id)
                    print(f"Заявка №{ticket_id} удалена")
                else:
                    print("Отменено")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "10":
            users = user_repo.get_all()
            roles = {1: "Админ", 2: "Оператор", 3: "Исполнитель", 4: "Заявитель"}
            print("\n--- Пользователи ---")
            for u in users:
                role = roles.get(u.role_id, "?")
                print(f"[{u.id}] {u.full_name} ({u.login}) — {role}")

        elif choice == "11":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()