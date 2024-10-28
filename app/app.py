import fastapi
from fastapi import HTTPException
import crud
import schema
from dependencies import SessionDependency
from lifespan import lifespan
from constants import STATUS_SUCCESS_RESPONSE


app = fastapi.FastAPI(lifespan=lifespan)

# Создать объявление
@app.post("/advertisement", response_model=schema.AdvertisementInDB)
async def create_advertisement(ad: schema.AdvertisementCreate, db: SessionDependency):
    return await crud.create_advertisement(db, ad)

# Обновить объявление
@app.patch("/advertisement/{ad_id}", response_model=schema.AdvertisementInDB)
async def update_advertisement(ad_id: int, ad: schema.AdvertisementUpdate, db: SessionDependency):
    db_ad = await crud.update_advertisement(db, ad_id, ad)
    if not db_ad:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_ad

# Удалить объявление
@app.delete("/advertisement/{ad_id}")
async def delete_advertisement(ad_id: int, db: SessionDependency):
    db_ad = await crud.delete_advertisement(db, ad_id)
    if not db_ad:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return STATUS_SUCCESS_RESPONSE

# Получить объявление по ID
@app.get("/advertisement/{ad_id}", response_model=schema.AdvertisementInDB)
async def get_advertisement(ad_id: int, db: SessionDependency):
    db_ad = await crud.get_advertisement(db, ad_id)
    if not db_ad:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_ad

# Поиск объявлений по параметрам
@app.get("/advertisement", response_model=list[schema.AdvertisementInDB])
async def search_advertisements(db: SessionDependency, **params: dict):
    return await crud.search_advertisements(db, params)