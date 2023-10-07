from pydantic import BaseModel

class StorageBase(BaseModel):
    price: float
    description: str
    amount: int
    product_id: int
    user_id: int

class CreateStorage(StorageBase):
    pass

class UpdateStorage(StorageBase):
    pass

class Storage(StorageBase):
    id: int

    class Config:
        orm_mode = True
