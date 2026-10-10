import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.repository.ticket_repository import TicketRepository
from src.service.ticket_service import TicketService


DB_PATH = os.path.join("docs", "db", "requests.db")


def get_service():
    repo = TicketRepository(DB_PATH)
    return TicketService(repo)


def test_get_all_tickets():
    """Проверка получения списка заявок."""
    service = get_service()
    tickets = service.get_all()
    assert isinstance(tickets, list)
    assert len(tickets) > 0


def test_get_ticket_by_id():
    """Проверка получения одной заявки."""
    service = get_service()
    ticket = service.get_by_id(1)
    assert ticket.id == 1
    assert ticket.title is not None


def test_create_ticket_validation():
    """Проверка валидации при создании."""
    service = get_service()
    try:
        service.create_ticket("", "описание", 1, 1)
        assert False, "Должно быть ValueError"
    except ValueError as e:
        assert "Тема не может быть пустой" in str(e)