from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str

class LoginUser(UserBase):
    pass

class RegisterUser(UserBase):
    name: str

class User(UserBase):
    class Config:
        orm_mode = True        
