from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Базовая схема объявления
class AdvertisementBase(BaseModel):
    title: str
    description: str
    price: float
    author: str

# Схема для создания объявления
class AdvertisementCreate(AdvertisementBase):
    pass

# Схема для обновления объявления
class AdvertisementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    author: Optional[str] = None

# Схема для отображения объявления в ответах
class AdvertisementInDB(AdvertisementBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True