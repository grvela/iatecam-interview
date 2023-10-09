from fastapi import HTTPException, Response

from app.schemas.storage import Storage, CreateStorage, UpdateStorage, StorageBase, RequestStorage
from app.schemas.product import CreateProduct
from app.schemas.tag import CreateTag

from app.repositories.storage import StorageRepository
from sqlalchemy.orm import Session
from typing import List

from app.services.product import ProductService
from app.services.tag import TagService

from app.config.session import AppService

class StorageService(AppService):
    def create_storage(self, storage: RequestStorage, user_id: int) -> Storage:
        product = CreateProduct(name=storage.product_name)
        tag = CreateTag(name=storage.tag_name)

        product_data = ProductService(self.db).create_product(product)
        tag_data = TagService(self.db).create_tag(tag)

        storage_data = CreateStorage(
            user_id=user_id,
            product_id=product_data.id,
            tag_id=tag_data.id,
            price=storage.price,
            description=storage.description,
            amount=storage.amount
        )

        return StorageRepository(self.db).create_storage(storage_data)

    def get_storage_by_id(self, storage_id: int) -> Storage:
        storage_data = StorageRepository(self.db).get_storage_by_id(storage_id)
        
        if not storage_data:
            raise HTTPException(status_code=404, detail="Storage not found")

        return storage_data

    def update_storage_by_id(self, storage_id: int, storage: UpdateStorage) -> Storage:
        storage_data = self.get_storage_by_id(storage_id)
        storage_data = storage
        return StorageRepository(self.db).update_storage(storage_data)

    def delete_storage_by_id(self, storage_id: int):
        storage_data = self.get_storage_by_id(storage_id)
        
        StorageRepository(self.db).delete_storage_by_id(storage_data.id)
        
        existing_storage = StorageRepository(self.db).get_storage_by_id(storage_id)
        
        if existing_storage:
            raise HTTPException(status_code=400, detail="Can't delete storage")
        
        return Response(status_code=204)

    def get_all_storages(self) -> List[Storage]:
        return StorageRepository(self.db).get_all_storages()
    
    def get_all_storages_by_user_id(self, user_id: int):
        return StorageRepository(self.db).get_all_storages_by_user_id(user_id)
    
    def get_all_storages_to_buy(self, user_id: int) -> List[Storage]:        
        products = StorageRepository(self.db).get_all_storages_to_buy(user_id)
        filtered_products = [product for product in products if product.amount > 0]
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(filtered_products)
        return filtered_products
