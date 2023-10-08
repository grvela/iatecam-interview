from fastapi import HTTPException

from app.schemas.storage import Storage, CreateStorage, UpdateStorage, StorageBase
from app.schemas.product import CreateProduct
from app.schemas.tag import CreateTag

from app.repositories.storage import StorageRepository
from sqlalchemy.orm import Session
from typing import List

from app.services.product import ProductService
from app.services.tag import TagService

from app.config.session import AppService

class StorageService(AppService):
    def create_storage(self, storage: CreateStorage) -> Storage:
        product = CreateProduct(name=storage.product_name)
        tag = CreateTag(name=storage.tag_name)

        product_data = ProductService(self.db).create_product(product)
        tag_data = TagService(self.db).create_tag(tag)

        storage_data = StorageBase(
            user_id=1,
            product_id=product_data.id,
            tag_id=tag_data.id,
            price=storage.price,
            description=storage.description,
            amount=storage.amount
        )

        return StorageRepository(self.db).create_storage(storage_data)

    def get_storage(self, storage_id: int) -> Storage:
        db_storage = StorageRepository(self.db).get_storage_by_id(storage_id)
        
        if not db_storage:
            raise HTTPException(status_code=404, detail="Storage not found")

        return db_storage

    def update_storage(self, storage_id: int, storage: UpdateStorage) -> Storage:
        db_storage = self.get_storage(storage_id)
        
        return StorageRepository(self.db).update_storage(storage_id, storage)

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
