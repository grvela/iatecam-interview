from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str

class CreateProduct(ProductBase):
    pass

class UpdateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
