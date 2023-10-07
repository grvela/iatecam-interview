from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.repositories.main import AbstractRepository

from typing import List

from app.schemas.user import User, CreateUser, UpdateUser

class UserRepository(AbstractRepository[UserModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = UserModel

    def create_user(self, user: CreateUser) -> User:
        return self._create(user)

    def get_user_by_id(self, user_id: int) -> User:
        return self._get(user_id)

    def update_user(self, user: UpdateUser) -> User:
       return self._update(user)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._delete(user_id)

    def get_all_users(self) -> List[User]:
        return self._get_all()
    
    def get_user_by_username(self, value: str) -> User:
        return self._search_one_with("username", value)
