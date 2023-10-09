from pydantic import BaseModel, conint

from app.schemas.product import Product
from app.schemas.tag import Tag

class StorageBase(BaseModel):
    price: float
    description: str
    amount: conint(ge=0)

class CreateStorage(BaseModel):
    product_name: str
    tag_name: str
    description: str
    price: float
    amount: conint(gt=0)

class UpdateStorage(BaseModel):
    price: float = None
    description: str = None

class Storage(StorageBase):
    id: int
    product: Product
    tag: Tag

    class Config:
        orm_mode = True
