from sqlalchemy.orm import Session
from app.models.storage import Storage as StorageModel
from app.repositories.main import AbstractRepository
from app.schemas.storage import Storage, CreateStorage, UpdateStorage, StorageBase

from typing import List

class StorageRepository(AbstractRepository[StorageModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = StorageModel

    def create_storage(self, storage: StorageBase) -> Storage:
        return self._create(storage)

    def get_storage_by_id(self, storage_id: int) -> Storage:
        return self._get(storage_id)

    def update_storage(self, storage: UpdateStorage) -> Storage:
        return self._update(storage)

    def delete_storage_by_id(self, storage_id: int) -> None:
        return self._delete(storage_id)

    def get_all_storages(self) -> List[Storage]:
        return self._get_all()