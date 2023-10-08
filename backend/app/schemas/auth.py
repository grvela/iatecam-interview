from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str

class LoginUser(UserBase):
    pass

class RegisterUser(UserBase):
    name: str

class UserCredentials(RegisterUser):
    id: int

    class Config:
        orm_mode = True        
