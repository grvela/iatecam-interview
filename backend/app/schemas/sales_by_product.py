from pydantic import BaseModel
from app.schemas.product import Product

class SalesByProductBase(BaseModel):
    amount: int

class CreateSalesByProduct(SalesByProductBase):
    product_id: int

class SalesByProduct(SalesByProductBase):
    id: int 
    product: Product

    class Config:
        orm_mode = True