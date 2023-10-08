from pydantic import BaseModel
from datetime import datetime

class OutputBase(BaseModel):
    amount: int
    storage_id: int
    user_id: int
    created_at: datetime

class CreateOutput(OutputBase):
    pass

class Output(OutputBase):
    id: int

    class Config:
        orm_mode = True
