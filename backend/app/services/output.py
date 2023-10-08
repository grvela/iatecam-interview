from fastapi import HTTPException, Response
from app.schemas.output import Output, CreateOutput
from app.repositories.output import OutputRepository
from app.repositories.storage import StorageRepository
from sqlalchemy.orm import Session
from typing import List

from app.config.session import AppService

class OutputService(AppService):
    def create_output(self, output: CreateOutput) -> Output:
        return OutputRepository(self.db).create_output(output)

    def get_output_by_id(self, output_id: int) -> Output:
        output_data = OutputRepository(self.db).get_output_by_id(output_id)
        
        if not output_data:
            raise HTTPException(status_code=404, detail="Output not found")

        return output_data

    def delete_output_by_id(self, output_id: int):
        output_data = self.get_output_by_id(output_id)
        
        OutputRepository(self.db).delete_output_by_id(output_data.id)
        
        existing_output = OutputRepository(self.db).get_output_by_id(output_data.id)
        
        if existing_output:
            raise HTTPException(status_code=400, detail="Can't delete output")
        
        return Response(status_code=204)

    def get_all_outputs(self) -> List[Output]:
        return OutputRepository(self.db).get_all_outputs()
    
    def get_all_outputs_by_user_id(self, user_id: int) -> List[Output]:
        return OutputRepository(self.db).get_all_outputs_by_user_id(user_id)

  #TODO  
    # def get_last_sells(self) -> List[Output]:
    #     ouput_data = OutputRepository(self.db).get_all_outputs


        