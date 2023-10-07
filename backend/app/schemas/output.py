from pydantic import BaseModel
from datetime import datetime

class OutputBase(BaseModel):
    amount: int
    created_at: datetime
    storage_id: int
    user_id: int

class CreateOutput(OutputBase):
    pass

class Output(OutputBase):
    id: int

    class Config:
        orm_mode = True
