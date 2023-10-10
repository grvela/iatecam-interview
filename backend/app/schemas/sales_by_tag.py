from pydantic import BaseModel
from app.schemas.tag import Tag

class SalesByTagBase(BaseModel):
    amount: int

class CreateSalesByTag(SalesByTagBase):
    tag_id: int

class SalesByTag(SalesByTagBase):
    id: int 
    tag: Tag

    class Config:
        orm_mode = True