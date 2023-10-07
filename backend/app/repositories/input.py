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
    
    def create_input(self, input_data: CreateInput) -> Input:
        input_obj = InputModel(
            storage_id=input_data.storage_id,
            client_id=input_data.client_id,
            amount=input_data.amount
        )
        return self._create(input_obj)
    
    def get_input(self, input_id: int) -> Input:
        return self._get(input_id)
    
    def update_input(self, input_data: CreateInput) -> Input:
        return self._update(input_data)
    
    def delete_input(self, input_id: int) -> None:
        self._delete(input_id)
    
    def get_all_inputs(self) -> List[Input]:
        return self._get_all()
    
    def search_inputs_by_field(self, field_name: str, value: str) -> List[Input]:
        return self._search_all_with(field_name, value)
    
    def search_input_by_field(self, field_name: str, value: str) -> Input:
        return self._search_one_with(field_name, value)
