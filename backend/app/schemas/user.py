from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class CreateUser(UserBase):
    name: str
    password: str

class UpdateUser(CreateUser):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True        
