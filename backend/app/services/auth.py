from app.config.session import AppService

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from app.services.user import UserService

from app.schemas.auth import RegisterUser, LoginUser

from app.utils.hash import Hash
from app.utils.jwt import JWTManager

class AuthService(AppService):
    def register_user(self, user_data: RegisterUser):
        user = UserService(self.db).create_user(user_data)
        return user
    
    def login_user(self, user_data: LoginUser):
        user = UserService(self.db).get_user_by_field(field_name="username", value=user_data.username)        

        equal_passwords = Hash.compare_hash(user_data.password, user.password)
        
        if not equal_passwords:
            raise HTTPException(status_code=400, detail="Credentials are not valid")
        
        jwt_manager = JWTManager()

        data = {
            "sub": user.username,
            "user_id": user.id
        }

        access_token = jwt_manager.create_token(data)

        return JSONResponse(content=access_token)

        
