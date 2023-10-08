from fastapi import HTTPException, Response
from app.schemas.input import Input, CreateInput
from app.repositories.input import InputRepository
from typing import List

from app.config.session import AppService

class InputService(AppService):    
    def create_input(self, input: CreateInput) -> Input:
        return InputRepository(self.db).create_input(input)
    
    def get_input_by_id(self, input_id: int) -> Input:
        input_data = InputRepository(self.db).get_input_by_id(input_id)
        
        if not input_data:
            raise HTTPException(status_code=404, detail="Input not found")

        return input_data

    def delete_input_by_id(self, input_id: int):
        input_data = self.get_input_by_id(input_id)
        
        InputRepository(self.db).delete_input_by_id(input_data.id)
        
        existing_input = InputRepository(self.db).get_input_by_id(input_data.id)
        
        if existing_input:
            raise HTTPException(status_code=400, detail="Can't delete input")
        
        return Response(status_code=204)

    def get_all_inputs(self) -> List[Input]:
        return InputRepository(self.db).get_all_inputs()
    
    def get_all_inputs_by_user_id(self, user_id: int) -> List[Input]:
        return InputRepository(self.db).get_all_inputs_by_user_id(user_id)
