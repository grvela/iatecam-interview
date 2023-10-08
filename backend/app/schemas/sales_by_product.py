from pydantic import BaseModel

class SalesByProductBase(BaseModel):
    product_id: int
    amount: int

class CreateSalesByProduct(SalesByProductBase):
    pass

class SalesByProduct(SalesByProductBase):
    id: int 

    class Config:
        orm_mode = True