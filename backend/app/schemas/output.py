from pydantic import BaseModel

class OutputBase(BaseModel):
    amount: int
    storage_id: int
    user_id: int

class CreateOutput(OutputBase):
    pass

class UpdateOutput(OutputBase):
    pass

class Output(OutputBase):
    id: int

    class Config:
        orm_mode = True
