from fastapi import HTTPException, Response
from app.config.session import AppService
from app.schemas.user import User, CreateUser, UpdateUser
from app.schemas.auth import UserCredentials
from app.repositories.user import UserRepository
from app.utils.hash import Hash
from typing import List

class UserService(AppService):
    def create_user(self, user: CreateUser) -> User:
        user_data = UserRepository(self.db).get_user_by_username(user.username)

        if user_data:
            raise HTTPException(status_code=409, detail="Username already exists")

        user.password = Hash.hash(user.password)
        
        return UserRepository(self.db).create_user(user)

    def get_user_by_id(self, user_id: int) -> User:
        user_data = UserRepository(self.db).get_user_by_id(user_id)
        
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")

        return user_data

    def update_user_by_id(self, user_id: int, user: UpdateUser) -> User:
        user_data = self.get_user_by_id(user_id)
        
        if user_data.username != user.username:
            existing_user = UserRepository(self.db).get_user_by_username(user.username)
            
            if existing_user:
                raise HTTPException(status_code=409, detail="Username already exists")

        return UserRepository(self.db).update_user(user)

    def delete_user_by_id(self, user_id: int) -> User:
        user_data = self.get_user_by_id(user_id)
        
        UserRepository(self.db).delete_user(user_data.id)
        
        existing_user = UserRepository(self.db).get_user_by_id(user_id)
        
        if existing_user:
            raise HTTPException(status_code=400, detail="Can't delete user")
        
        return Response(status_code=204)

    def get_all_users(self) -> List[User]:
        return UserRepository(self.db).get_all_users()
    
    def get_user_by_username(self, value: str) -> User:
        return UserRepository(self.db).get_user_by_username(value)
    
    def get_user_credentials(self, username: str) -> UserCredentials:
        return UserRepository(self.db).get_user_credentials(username)