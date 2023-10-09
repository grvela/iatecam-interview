from sqlalchemy import desc
from sqlalchemy.orm import Session, joinedload
from typing import TypeVar, Generic, List
from sqlalchemy.ext.declarative import DeclarativeMeta


ModelType = TypeVar("ModelType")

class AbstractRepository(Generic[ModelType]):    
    def __init__(self, db: Session):
        self.db = db

    def _create(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def _get(self, id: int) -> ModelType:
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def _update(self, entity: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def _delete(self, id: int) -> None:
        entity = self._get(id)
        if entity:
            self.db.delete(entity)
            self.db.commit()
   
    def _get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()

    def _search_all_without(self, field_name: str, value: str) -> List[ModelType]:
        return self.db.query(self.model).filter(getattr(self.model, field_name) != value).all()

    def _search_all_with(self, field_name: str, value: str) -> List[ModelType]:
        return self.db.query(self.model).filter(getattr(self.model, field_name) == value).all()
    
    def _search_one_with(self, field_name: str, value: str) -> List[ModelType]:
        return self.db.query(self.model).filter(getattr(self.model, field_name) == value).first()
    
    def _get_last_n_records(self, field_name: str, n: int):
        return self.db.query(self.model).order_by(desc(getattr(self.model, field_name))).limit(n).all()