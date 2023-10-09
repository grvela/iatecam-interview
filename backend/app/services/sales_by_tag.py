from app.config.session import AppService

from app.schemas.sales_by_tag import CreateSalesByTag, SalesByTag
from app.repositories.sales_by_tag import SalesByTagRepository

from typing import List

class SalesByTagService(AppService):
    def create_sales(self, sales: CreateSalesByTag) -> SalesByTag:
        sales_data = SalesByTagRepository(self.db).get_sale_by_tag_id(sales.tag_id)

        if sales_data:
            return sales_data
        
        return SalesByTagRepository(self.db).create_sales_by_tag(sales)

    def get_sales_by_tag(self) -> List[SalesByTag]:
        return SalesByTagRepository(self.db).get_sales_by_tag()

    def add_to_analytics(self, tag_id: int, amount: int) -> SalesByTag:
        sale = CreateSalesByTag(tag_id=tag_id, amount=amount)

        sales_data = self.create_sales(sale)

        sales_data.amount = sales_data.amount + amount

        return sales_data