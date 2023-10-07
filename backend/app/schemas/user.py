from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    username: str

class CreateUser(UserBase):
    password: str

class UpdateUser(BaseModel):
    name: str = None
    username: str = None
    password: str = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True        
