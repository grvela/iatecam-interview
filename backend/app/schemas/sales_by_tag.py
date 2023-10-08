from pydantic import BaseModel

class SalesByTagBase(BaseModel):
    tag_id: int
    amount: int

class CreateSalesByTag(SalesByTagBase):
    pass

class SalesByTag(SalesByTagBase):
    id: int 

    class Config:
        orm_mode = True