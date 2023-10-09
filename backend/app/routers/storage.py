from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.storage import StorageService
from app.schemas.storage import Storage, CreateStorage, UpdateStorage, RequestStorage
from typing import List

from app.middlewares.auth import get_current_user

router = APIRouter(
    prefix="/storages",
    tags=["Storage"]
)

@router.post("/", response_model=Storage)
def create_storage(storage_data: RequestStorage, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return StorageService(db).create_storage(storage_data, current_user["user_id"])

@router.get("/by/me", response_model=List[Storage])
def get_all_user_storages(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return StorageService(db).get_all_storages_by_user_id(current_user["user_id"])

@router.get("/to/me", response_model=List[Storage])
def get_all_storages_to_buy(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return StorageService(db).get_all_storages_to_buy(current_user["user_id"])

@router.get("/{storage_id}", response_model=Storage)
def get_storage(storage_id: int, db: Session = Depends(get_db)):
    return StorageService(db).get_storage_by_id(storage_id)

@router.put("/{storage_id}", response_model=Storage)
def update_storage(storage_id: int, storage_data: UpdateStorage, db: Session = Depends(get_db)):
    return StorageService(db).update_storage_by_id(storage_id, storage_data)

@router.delete("/{storage_id}")
def delete_storage(storage_id: int, db: Session = Depends(get_db)):
    return StorageService(db).delete_storage_by_id(storage_id)

@router.get("/", response_model=List[Storage])
def get_all_storages(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return StorageService(db).get_all_storages()