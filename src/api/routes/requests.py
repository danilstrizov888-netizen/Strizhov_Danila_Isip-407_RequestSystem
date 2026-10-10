from fastapi import APIRouter, HTTPException, Query
from typing import List
from src.api.schemas import TicketCreate, TicketUpdate, TicketOut
from src.repository.ticket_repository import TicketRepository
from src.service.ticket_service import TicketService
import os

router = APIRouter(prefix="/requests", tags=["Заявки"])

db_path = os.path.join("docs", "db", "requests.db")
ticket_repo = TicketRepository(db_path)
ticket_service = TicketService(ticket_repo)


@router.get("/", response_model=List[TicketOut])
def get_requests(status_id: int | None = Query(None, description="Фильтр по статусу")):
    """Список заявок с фильтром по статусу."""
    if status_id is not None:
        return ticket_service.filter_by_status(status_id)
    return ticket_service.get_all()


@router.get("/{ticket_id}", response_model=TicketOut)
def get_request(ticket_id: int):
    """Получить заявку по ID."""
    try:
        return ticket_service.get_by_id(ticket_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=TicketOut, status_code=201)
def create_request(data: TicketCreate):
    """Создать новую заявку."""
    try:
        return ticket_service.create_ticket(
            title=data.title,
            description=data.description,
            category_id=data.category_id,
            author_id=data.author_id
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.patch("/{ticket_id}", response_model=TicketOut)
def update_request(ticket_id: int, data: TicketUpdate):
    """Обновить заявку."""
    try:
        ticket = ticket_service.get_by_id(ticket_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        if data.title is not None:
            description = data.description if data.description is not None else ticket.description
            ticket_service.update_ticket(ticket_id, data.title, description or "")

        if data.status_id is not None:
            ticket_service.change_status(ticket_id, data.status_id)

        if data.assignee_id is not None:
            ticket_service.assign_executor(ticket_id, data.assignee_id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

    return ticket_service.get_by_id(ticket_id)


@router.delete("/{ticket_id}", status_code=204)
def delete_request(ticket_id: int):
    """Удалить заявку."""
    try:
        ticket_service.delete_ticket(ticket_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return None