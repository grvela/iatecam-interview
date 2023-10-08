from fastapi import HTTPException
from app.schemas.input import Input, CreateInput
from app.repositories.input import InputRepository
from typing import List

from app.config.session import AppService

from app.services.storage import StorageService
from app.schemas.storage import CreateStorage

class InputService(AppService):    
    def create_input(self, input_data: CreateInput) -> Input:
        pass
    
    def get_input(self, input_id: int) -> Input:
        db_input = InputRepository(self.db).get_input(input_id)
        
        if not db_input:
            raise HTTPException(status_code=404, detail="Input not found")

        return db_input

    def delete_input(self, input_id: int):
        db_input = self.get_input(input_id)
        
        InputRepository(self.db).delete_input(db_input.id)
        
        existing_input = InputRepository(self.db).get_input(input_id)
        
        if existing_input:
            raise HTTPException(status_code=400, detail="Can't delete input")

    def get_all_inputs(self) -> List[Input]:
        return InputRepository(self.db).get_all_inputs()
    
    def get_input_by_field(self, field_name: str, value: str) -> Input:
        input_data = InputRepository(self.db).search_input_by_field(field_name, value)

        if not input_data:
            raise HTTPException(status_code=404, detail="Input not found")
        
        return input_data
