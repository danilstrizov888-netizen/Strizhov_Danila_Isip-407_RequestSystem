from pydantic import BaseModel, Field


# ---------- Схемы для заявок ----------

class TicketBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Тема заявки")
    description: str = Field("", max_length=1000, description="Описание")
    category_id: int = Field(..., ge=1, description="ID категории")
    author_id: int = Field(..., ge=1, description="ID автора")


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=1000)
    category_id: int | None = Field(None, ge=1)
    status_id: int | None = Field(None, ge=1, le=4)
    assignee_id: int | None = Field(None, ge=1)


class TicketOut(BaseModel):
    id: int
    title: str
    description: str | None
    category_id: int
    status_id: int
    author_id: int
    assignee_id: int | None = None

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id: int
    login: str
    full_name: str
    role_id: int

    class Config:
        from_attributes = True


class StatusOut(BaseModel):
    id: int
    name: str


class CategoryOut(BaseModel):
    id: int
    name: str


class ErrorResponse(BaseModel):
    detail: str