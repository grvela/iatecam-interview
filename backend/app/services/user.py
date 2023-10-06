from fastapi import HTTPException, Response
from app.config.session import AppService
from app.schemas.user import User, CreateUser, UpdateUser
from app.repositories.user import UserRepository
from typing import List

class UserService(AppService):
    def create_user(self, user_data: CreateUser) -> User:
        db_user = UserRepository(self.db).search_user_by_field('username', user_data.username)
        
        if db_user:
            raise HTTPException(status_code=409, detail="Username already exists")

        return UserRepository(self.db).create_user(user_data)

    def get_user(self, user_id: int) -> User:
        db_user = UserRepository(self.db).get_user_by_id(user_id)
        
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        return db_user

    def update_user(self, user_id: int, user_data: UpdateUser) -> User:
        db_user = self.get_user(user_id)
        
        if user_data.username != db_user.username:
            existing_user = UserRepository(self.db).search_user_by_field('username', user_data.username)
            
            if existing_user:
                raise HTTPException(status_code=409, detail="Username already exists")

        return UserRepository(self.db).update_user(user_data)

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        
        UserRepository(self.db).delete_user(db_user.id)
        
        existing_user = UserRepository(self.db).get_user_by_id(user_id)
        
        if existing_user:
            raise HTTPException(status_code=400, detail="Can't delete user")
        
        return Response(status_code=204)

    def get_all_users(self) -> List[User]:
        return UserRepository(self.db).get_all_users()
