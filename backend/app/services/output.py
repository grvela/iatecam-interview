from fastapi import HTTPException
from app.schemas.output import Output, CreateOutput
from app.repositories.output import OutputRepository
from sqlalchemy.orm import Session
from typing import List

from app.config.session import AppService

class OutputService(AppService):
    def create_output(self, output_data: CreateOutput) -> Output:
        db_output = OutputRepository(self.db).search_output_by_field('storage_id', output_data.storage_id)
        
        if db_output:
            raise HTTPException(status_code=409, detail="Output already exists")

        return OutputRepository(self.db).create_output(output_data)

    def get_output(self, output_id: int) -> Output:
        db_output = OutputRepository(self.db).get_output_by_id(output_id)
        
        if not db_output:
            raise HTTPException(status_code=404, detail="Output not found")

        return db_output

    def delete_output(self, output_id: int):
        db_output = self.get_output(output_id)
        
        OutputRepository(self.db).delete_output(db_output.id)
        
        existing_output = OutputRepository(self.db).get_output_by_id(output_id)
        
        if existing_output:
            raise HTTPException(status_code=400, detail="Can't delete output")

    def get_all_outputs(self) -> List[Output]:
        return OutputRepository(self.db).get_all_outputs()
    
    def get_output_by_field(self, field_name: str, value: str) -> Output:
        output_data = OutputRepository(self.db).search_output_by_field(field_name, value)

        if not output_data:
            raise HTTPException(status_code=404, detail="Output not found")
        
        return output_data
