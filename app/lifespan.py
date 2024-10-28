from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("START")
    # Инициализация базы данных при запуске приложения
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Закрытие соединения с базой данных при завершении работы приложения
    await engine.dispose()
    print("FINISH")