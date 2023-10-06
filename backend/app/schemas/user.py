from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    username: str
    role: str = "client"

class CreateUser(UserBase):
    password: str


class UpdateUser(CreateUser):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True        
