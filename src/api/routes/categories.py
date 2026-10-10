from fastapi import APIRouter
from typing import List
from src.api.schemas import CategoryOut

router = APIRouter(prefix="/categories", tags=["Справочники"])


@router.get("/", response_model=List[CategoryOut])
def get_categories():
    """Справочник категорий."""
    return [
        {"id": 1, "name": "IT"},
        {"id": 2, "name": "Хозяйство"},
        {"id": 3, "name": "Документы"},
        {"id": 4, "name": "Ремонт"},
    ]