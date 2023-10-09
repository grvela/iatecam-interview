from pydantic import BaseModel, conint

from app.schemas.product import Product
from app.schemas.tag import Tag
from app.schemas.user import User

class StorageBase(BaseModel):
    price: float
    description: str
    amount: conint(ge=0)

class RequestStorage(StorageBase):
    product_name: str
    tag_name: str

class CreateStorage(StorageBase):
    user_id: int
    product_id: int
    tag_id: int 

class UpdateStorage(BaseModel):
    price: float = None
    description: str = None

class Storage(StorageBase):
    id: int
    product: Product
    tag: Tag
    user: User

    class Config:
        orm_mode = True
