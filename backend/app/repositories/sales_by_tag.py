from app.models.sales_by_tag import SalesByTag as SalesByTagModel

from app.schemas.sales_by_tag import SalesByTag, CreateSalesByTag

from app.repositories.main import AbstractRepository
from sqlalchemy.orm import Session

from typing import List

class SalesByTagRepository(AbstractRepository[SalesByTagModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = SalesByTagModel

    def create_sales_by_tag(self, sales: CreateSalesByTag):
        entity = SalesByTagModel(
            tag_id=sales.tag_id,
            amount=0
        )
        return self._create(entity)
    
    def get_sale_by_tag_id(self, tag_id: int) -> SalesByTag:
        return self._search_one_with("tag_id", tag_id)
    
    def get_sales_by_tag(self) -> List[SalesByTag]:
        return self._get_all()