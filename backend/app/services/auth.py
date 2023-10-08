from app.config.session import AppService

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from app.services.user import UserService

from app.schemas.user import CreateUser
from app.schemas.auth import RegisterUser, LoginUser

from app.utils.hash import Hash
from app.utils.jwt import JWTManager

class AuthService(AppService):
    def register_user(self, user: RegisterUser):
        user_data = CreateUser(
            name=user.name,
            username=user.username,
            password=user.password
        )
        return UserService(self.db).create_user(user_data)
        
    
    def login_user(self, user: LoginUser):
        user_data = UserService(self.db).get_user_credentials(user.username)

        equal_passwords = Hash.compare_hash(user.password, user_data.password)
        
        if not equal_passwords:
            raise HTTPException(status_code=400, detail="Credentials are not valid")
        
        data = {
            "sub": user_data.username,
            "user_id": user_data.id
        }

        access_token = JWTManager().create_token(data)


        return { "access_token": access_token, "token_type": "bearer" }

        
