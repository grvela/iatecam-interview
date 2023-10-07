from sqlalchemy.orm import Session
from app.models.storage import Storage as StorageModel
from app.repositories.main import AbstractRepository
from app.schemas.storage import Storage, CreateStorage, UpdateStorage

class StorageRepository(AbstractRepository[StorageModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = StorageModel

    def create_storage(self, storage_data: CreateStorage) -> Storage:
        storage = StorageModel(
            price=storage_data.price,
            description=storage_data.description,
            amount=storage_data.amount,
            product_id=storage_data.product_id,
            user_id=storage_data.user_id
        )
        return self._create(storage)

    def get_storage_by_id(self, storage_id: int) -> Storage:
        return self._get(storage_id)

    def update_storage(self, storage_data: UpdateStorage) -> Storage:
        return self._update(storage_data)

    def delete_storage(self, storage_id: int):
        return self._delete(storage_id)

    def get_all_storages(self):
        return self._get_all()

    def search_storages_by_field(self, field_name, value):
        return self._search_all_with(field_name, value)

    def search_storage_by_field(self, field_name, value):
        return self._search_one_with(field_name, value)
