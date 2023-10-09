from app.config.session import AppService

from app.schemas.sales_by_product import CreateSalesByProduct, SalesByProduct
from app.repositories.sales_by_product import SalesByProductRepository

from typing import List

class SalesByProductService(AppService):
    def create_sales(self, sales: CreateSalesByProduct) -> SalesByProduct:
        sales_data = SalesByProductRepository(self.db).get_sale_by_product_id(sales.product_id)

        if sales_data:
            return sales_data
        
        return SalesByProductRepository(self.db).create_sales_by_product(sales)
    
    def get_sales_by_product(self) -> List[SalesByProduct]:
        return SalesByProductRepository(self.db).get_sales_by_product()

    def add_to_analytics(self, product_id: int, amount: int) -> SalesByProduct:
        sale = CreateSalesByProduct(product_id=product_id, amount=amount)

        sales_data = self.create_sales(sale)

        sales_data.amount = sales_data.amount + amount

        return sales_data