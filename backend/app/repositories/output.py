from sqlalchemy.orm import Session
from app.models.output import Output as OutputModel
from app.repositories.main import AbstractRepository
from app.schemas.output import Output, CreateOutput, UpdateOutput

class OutputRepository(AbstractRepository[OutputModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = OutputModel

    def create_output(self, output_data: CreateOutput) -> Output:
        output = OutputModel(
            amount=output_data.amount,
            storage_id=output_data.storage_id,
            user_id=output_data.user_id
        )
        return self._create(output)

    def get_output_by_id(self, output_id: int) -> Output:
        return self._get(output_id)

    def update_output(self, output_data: UpdateOutput) -> Output:
        return self._update(output_data)

    def delete_output(self, output_id):
        return self._delete(output_id)

    def get_all_outputs(self):
        return self._get_all()

    def search_outputs_by_field(self, field_name, value):
        return self._search_all_with(field_name, value)

    def search_output_by_field(self, field_name, value):
        return self._search_one_with(field_name, value)
