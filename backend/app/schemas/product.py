from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    tag_id: int

class CreateProduct(ProductBase):
    pass

class UpdateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
