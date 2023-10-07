from sqlalchemy.orm import Session
from app.models.output import Output as OutputModel
from app.repositories.main import AbstractRepository
from app.schemas.output import Output, CreateOutput

from typing import List

class OutputRepository(AbstractRepository[OutputModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = OutputModel

    def create_output(self, output: CreateOutput) -> Output:
        return self._create(output)

    def get_output_by_id(self, output_id: int) -> Output:
        return self._get(output_id)

    def delete_output_by_id(self, output_id: int) -> Output:
        return self._delete(output_id)

    def get_all_outputs(self) -> List[Output]:
        return self._get_all()
