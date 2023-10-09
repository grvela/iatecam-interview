from pydantic import BaseModel
from datetime import datetime

from app.schemas.user import User
from app.schemas.storage import Storage

class OutputBase(BaseModel):
    amount: int
    created_at: datetime

class CreateOutput(OutputBase):
    pass

class Output(OutputBase):
    id: int
    user: User
    storage: Storage

    class Config:
        orm_mode = True
