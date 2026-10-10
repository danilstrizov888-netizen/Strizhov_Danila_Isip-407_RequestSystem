from fastapi import APIRouter
from typing import List
from src.api.schemas import UserOut
from src.repository.user_repository import UserRepository
import os

router = APIRouter(prefix="/users", tags=["Пользователи"])

db_path = os.path.join("docs", "db", "requests.db")
user_repo = UserRepository(db_path)


@router.get("/", response_model=List[UserOut])
def get_users():
    """Список всех пользователей."""
    return user_repo.get_all()