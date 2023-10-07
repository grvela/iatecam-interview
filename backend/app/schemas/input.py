from pydantic import BaseModel

class InputBase(BaseModel):
    amount: int
    storage_id: int
    user_id: int

class CreateInput(InputBase):
    pass

class UpdateInput(InputBase):
    pass

class Input(InputBase):
    id: int

    class Config:
        orm_mode = True
