from pydantic import BaseModel, conint
from datetime import datetime

class InputBase(BaseModel):
    amount: conint(gt=0)
    created_at: datetime
    storage_id: int
    user_id: int

class CreateInput(InputBase):
    pass

class Input(InputBase):
    id: int

    class Config:
        orm_mode = True
