from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models import Advertisement
from schema import AdvertisementCreate, AdvertisementUpdate

# Получить объявление по id
async def get_advertisement(db: Session, ad_id: int):
    result = await db.execute(select(Advertisement).filter(Advertisement.id == ad_id))
    return result.scalars().first()

# Создать объявление
async def create_advertisement(db: Session, ad: AdvertisementCreate):
    db_ad = Advertisement(**ad.dict())
    db.add(db_ad)
    await db.commit()
    await db.refresh(db_ad)
    return db_ad

# Обновить объявление
async def update_advertisement(db: Session, ad_id: int, ad_data: AdvertisementUpdate):
    db_ad = await get_advertisement(db, ad_id)
    if not db_ad:
        return None
    for key, value in ad_data.dict(exclude_unset=True).items():
        setattr(db_ad, key, value)
    await db.commit()
    return db_ad

# Удалить объявление
async def delete_advertisement(db: Session, ad_id: int):
    db_ad = await get_advertisement(db, ad_id)
    if db_ad:
        await db.delete(db_ad)
        await db.commit()
    return db_ad

# Поиск объявлений по параметрам
async def search_advertisements(db: Session, query_params: dict):
    query = select(Advertisement)
    for key, value in query_params.items():
        query = query.filter(getattr(Advertisement, key).ilike(f"%{value}%"))
    result = await db.execute(query)
    return result.scalars().all()