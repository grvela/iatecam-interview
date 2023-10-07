from pydantic import BaseModel, conint

class StorageBase(BaseModel):
    user_id: int
    product_id: int
    tag_id: int
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

    class Config:
        orm_mode = True
