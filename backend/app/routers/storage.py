from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.storage import StorageService
from app.schemas.storage import Storage, CreateStorage, UpdateStorage
from typing import List

router = APIRouter(
    prefix="/storages",
    tags=["Storage"]
)

@router.post("/", response_model=Storage)
def create_storage(storage_data: CreateStorage, db: Session = Depends(get_db)):
    return StorageService(db).create_storage(storage_data)

@router.get("/{storage_id}", response_model=Storage)
def get_storage(storage_id: int, db: Session = Depends(get_db)):
    return StorageService(db).get_storage(storage_id)

@router.put("/{storage_id}", response_model=Storage)
def update_storage(storage_id: int, storage_data: UpdateStorage, db: Session = Depends(get_db)):
    return StorageService(db).update_storage(storage_id, storage_data)

@router.delete("/{storage_id}")
def delete_storage(storage_id: int, db: Session = Depends(get_db)):
    return StorageService(db).delete_storage(storage_id)

@router.get("/", response_model=List[Storage])
def read_all_storages(db: Session = Depends(get_db)):
    return StorageService(db).get_all_storages()