from fastapi import HTTPException
from app.schemas.storage import Storage, CreateStorage, UpdateStorage
from app.repositories.storage import StorageRepository
from sqlalchemy.orm import Session
from typing import List

from app.config.session import AppService

class StorageService(AppService):
    def create_storage(self, storage_data: CreateStorage) -> Storage:
        db_storage = StorageRepository(self.db).search_storage_by_field('product_id', storage_data.product_id)
        
        if db_storage:
            raise HTTPException(status_code=409, detail="Storage already exists")

        return StorageRepository(self.db).create_storage(storage_data)

    def get_storage(self, storage_id: int) -> Storage:
        db_storage = StorageRepository(self.db).get_storage_by_id(storage_id)
        
        if not db_storage:
            raise HTTPException(status_code=404, detail="Storage not found")

        return db_storage

    def update_storage(self, storage_id: int, storage_data: UpdateStorage) -> Storage:
        db_storage = self.get_storage(storage_id)
        
        return StorageRepository(self.db).update_storage(storage_id, storage_data)

    def delete_storage(self, storage_id: int):
        db_storage = self.get_storage(storage_id)
        
        StorageRepository(self.db).delete_storage(db_storage.id)
        
        existing_storage = StorageRepository(self.db).get_storage_by_id(storage_id)
        
        if existing_storage:
            raise HTTPException(status_code=400, detail="Can't delete storage")

    def get_all_storages(self) -> List[Storage]:
        return StorageRepository(self.db).get_all_storages()
    
    def get_storage_by_field(self, field_name: str, value: str) -> Storage:
        return StorageRepository(self.db).search_storage_by_field(field_name, value)
