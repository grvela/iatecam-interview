from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
