from sqlalchemy.orm import Session, joinedload
from app.models.storage import Storage as StorageModel
from app.repositories.main import AbstractRepository
from app.schemas.storage import Storage, CreateStorage, UpdateStorage, StorageBase

from typing import List

class StorageRepository(AbstractRepository[StorageModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = StorageModel

    def create_storage(self, storage: CreateStorage) -> Storage:
        entity = StorageModel(
            user_id=storage.user_id,
            product_id=storage.product_id,
            tag_id=storage.tag_id,
            price=storage.price,
            description=storage.description,
            amount=storage.amount
        )
        return self._create(entity)

    def get_storage_by_id(self, storage_id: int) -> Storage:
        return self._get(storage_id)

    def update_storage(self, storage: UpdateStorage) -> Storage:
        return self._update(storage)

    def delete_storage_by_id(self, storage_id: int) -> None:
        return self._delete(storage_id)

    def get_all_storages(self) -> List[Storage]:
        return self._get_all()
    
    def get_all_storages_by_user_id(self, user_id: int) -> List[Storage]:
        return self._search_all_with("user_id", user_id)
    
    def get_all_storages_to_buy(self, user_id: int) -> List[Storage]:
        return self._search_all_without("user_id", user_id)