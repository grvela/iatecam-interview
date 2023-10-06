from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.repositories.main import AbstractRepository

from app.schemas.user import User, CreateUser, UpdateUser

class UserRepository(AbstractRepository[UserModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = UserModel

    def create_user(self, user_data: CreateUser) -> User:
        user = UserModel(
            name=user_data.name,
            username=user_data.username,
            password=user_data.password,
            role=user_data.role,
        )
        return self._create(user)

    def get_user_by_id(self, user_id: int) -> User:
        return self._get(user_id)

    def update_user(self, user_data: UpdateUser) -> User:
       return self._update(user_data)

    def delete_user(self, user_id):
        return self._delete(user_id)

    def get_all_users(self):
        return self._get_all()

    def search_users_by_field(self, field_name, value):
        return self._search_all_with(field_name, value)

    def search_user_by_field(self, field_name, value):
        return self._search_one_with(field_name, value)
