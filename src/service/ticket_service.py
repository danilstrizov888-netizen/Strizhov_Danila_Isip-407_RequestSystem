class TicketService:
    def __init__(self, ticket_repo):
        self.ticket_repo = ticket_repo

    def create_ticket(self, title, description, category_id, author_id):
        # Валидация
        if not title or len(title.strip()) == 0:
            raise ValueError("Тема не может быть пустой")
        if len(title) > 200:
            raise ValueError("Тема слишком длинная")

        from src.models.ticket import Ticket
        ticket = Ticket(
            id=None,
            title=title.strip(),
            description=description.strip(),
            category_id=category_id,
            status_id=1,  # Новая
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
        self.get_by_id(ticket_id)  # проверка существования
        self.ticket_repo.update_status(ticket_id, status_id)