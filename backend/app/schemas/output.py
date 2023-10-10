from pydantic import BaseModel
from datetime import datetime

from app.schemas.user import User
from app.schemas.storage import Storage

class OutputBase(BaseModel):
    amount: int

class CreateOutput(OutputBase):
    storage_id: int
    user_id: int

class Output(OutputBase):
    id: int
    user: User
    storage: Storage
    created_at: datetime

    class Config:
        orm_mode = True
