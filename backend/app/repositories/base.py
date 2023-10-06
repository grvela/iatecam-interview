from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import TypeVar, Generic, List
''
ModelType = TypeVar("ModelType")

class AbstractRepository(Generic[ModelType], ABC):
    def __init__(self, db: Session):
        self.db = db

    def create(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get(self, id: int) -> ModelType:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def update(self, entity: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, id: int) -> None:
        entity = self.get(id)
        if entity:
            self.db.delete(entity)
            self.db.commit()

    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()
