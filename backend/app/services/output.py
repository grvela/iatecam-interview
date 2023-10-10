from fastapi import HTTPException, Response
from app.schemas.output import Output, CreateOutput
from app.repositories.output import OutputRepository
from typing import List
from app.services.storage import StorageService

from app.services.sales_by_tag import SalesByTagService
from app.services.sales_by_product import SalesByProductService

from app.config.session import AppService

class OutputService(AppService):
    def create_output(self, user_id: int, output: CreateOutput) -> Output:
        storage_data = StorageService(self.db).get_storage_by_id(output.storage_id)

        if storage_data.amount < output.amount:
            raise HTTPException(status_code=400, detail="No storage for this product")
        
        storage_data.amount = storage_data.amount - output.amount

        SalesByTagService(self.db).add_to_analytics(storage_data.tag.id, output.amount)
        SalesByProductService(self.db).add_to_analytics(storage_data.product.id, output.amount)
        
        return OutputRepository(self.db).create_output(user_id, output)

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

    def get_last_sells(self) -> List[Output]:
        return OutputRepository(self.db).get_last_outputs()


        