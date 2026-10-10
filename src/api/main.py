from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.api.routes import requests, users, statuses, categories


app = FastAPI(
    title="Система учёта заявок",
    description="REST API для системы учёта заявок",
    version="1.0.0"
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Внутренняя ошибка сервера"}
    )


app.include_router(requests.router)
app.include_router(users.router)
app.include_router(statuses.router)
app.include_router(categories.router)


@app.get("/health", tags=["Главная"])
def health():
    """Проверка работоспособности."""
    return {"status": "ok"}


@app.get("/", tags=["Главная"])
def root():
    """Проверка работоспособности API."""
    return {
        "message": "Система учёта заявок API",
        "docs": "/docs",
        "version": "1.0.0"
    }