from fastapi import APIRouter
from typing import List
from src.api.schemas import StatusOut

router = APIRouter(prefix="/statuses", tags=["Справочники"])


@router.get("/", response_model=List[StatusOut])
def get_statuses():
    """Справочник статусов."""
    return [
        {"id": 1, "name": "Новая"},
        {"id": 2, "name": "В работе"},
        {"id": 3, "name": "Выполнена"},
        {"id": 4, "name": "Закрыта"},
    ]