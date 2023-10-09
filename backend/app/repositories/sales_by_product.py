from app.models.sales_by_product import SalesByProduct as SalesByProductModel

from app.schemas.sales_by_product import SalesByProduct, CreateSalesByProduct

from app.repositories.main import AbstractRepository
from sqlalchemy.orm import Session

from typing import List

class SalesByProductRepository(AbstractRepository[SalesByProductModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = SalesByProductModel

    def create_sales_by_product(self, sales: CreateSalesByProduct):
        entity = SalesByProductModel(
            product_id=sales.product_id,
            amount=0
        )
        return self._create(entity)
    
    def get_sale_by_product_id(self, product_id: int) -> SalesByProduct:
        return self._search_one_with("product_id", product_id)
    
    def get_sales_by_product(self) -> List[SalesByProduct]:
        return self._get_all()