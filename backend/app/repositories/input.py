from app.config.database import Base
from app.models.input import Input as InputModel

from app.schemas.input import Input, CreateInput

from sqlalchemy.orm import Session
from typing import List
from app.repositories.main import AbstractRepository

class InputRepository(AbstractRepository[InputModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = InputModel
    
    def create_input(self, input: CreateInput) -> Input:
        entity = InputModel(
            user_id=input.user_id,
            storage_id=input.storage_id,
            amount=input.amount,
            created_at=input.created_at
        )
        return self._create(entity)
    
    def get_input_by_id(self, input_id: int) -> Input:
        return self._get(input_id)
    
    def delete_input_by_id(self, input_id: int) -> None:
        self._delete(input_id)
    
    def get_all_inputs(self) -> List[Input]:
        return self._get_all()
