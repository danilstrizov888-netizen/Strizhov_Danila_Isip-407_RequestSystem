import os
from src.models.ticket import Ticket
from src.repository.user_repository import UserRepository


class TicketService:
    def __init__(self, ticket_repo):
        self.ticket_repo = ticket_repo

    def create_ticket(self, title, description, category_id, author_id):
        # Валидация темы
        if not title or len(title.strip()) == 0:
            raise ValueError("Тема не может быть пустой")
        if len(title) > 200:
            raise ValueError("Тема слишком длинная")

        # Проверка автора (BUG-01 fix)
        db_path = os.path.join("docs", "db", "requests.db")
        user_repo = UserRepository(db_path)
        user = user_repo.get_by_id(author_id)
        if not user:
            raise ValueError(f"Пользователь с id={author_id} не найден")

        ticket = Ticket(
            id=None,
            title=title.strip(),
            description=description.strip(),
            category_id=category_id,
            status_id=1,
            author_id=author_id
        )
        return self.ticket_repo.create(ticket)

    def get_all(self):
        return self.ticket_repo.get_all()

    def get_by_id(self, ticket_id):
        ticket = self.ticket_repo.get_by_id(ticket_id)
        if not ticket:
            raise ValueError(f"Заявка с id={ticket_id} не найдена")
        return ticket

    def change_status(self, ticket_id, status_id):
        self.get_by_id(ticket_id)
        self.ticket_repo.update_status(ticket_id, status_id)

    def assign_executor(self, ticket_id, assignee_id):
        self.get_by_id(ticket_id)
        self.ticket_repo.update_assignee(ticket_id, assignee_id)

    def update_ticket(self, ticket_id, title, description):
        if not title or len(title.strip()) == 0:
            raise ValueError("Тема не может быть пустой")
        if len(title) > 200:
            raise ValueError("Тема слишком длинная")
        self.get_by_id(ticket_id)
        self.ticket_repo.update(ticket_id, title.strip(), description.strip())

    def delete_ticket(self, ticket_id):
        self.get_by_id(ticket_id)
        self.ticket_repo.delete(ticket_id)

    def search(self, query):
        if not query or len(query.strip()) == 0:
            raise ValueError("Поисковый запрос не может быть пустым")
        return self.ticket_repo.search(query.strip())

    def filter_by_status(self, status_id):
        return self.ticket_repo.filter_by_status(status_id)

    def filter_by_category(self, category_id):
        return self.ticket_repo.filter_by_category(category_id)