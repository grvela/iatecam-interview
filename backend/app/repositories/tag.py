from app.schemas.tag import CreateTag, UpdateTag, Tag
from app.models.tag import Tag as TagModel
from app.repositories.main import AbstractRepository

from sqlalchemy.orm import Session

from typing import List


class TagRepository(AbstractRepository[TagModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = TagModel

    def create_tag(self, tag: CreateTag) -> Tag:
        tag = TagModel(name=tag.name)
        return self._create(tag)

    def get_tag_by_id(self, tag_id: int) -> Tag:
        return self._get(tag_id)
    
    def update_tag(self, tag: UpdateTag) -> Tag:
        return self._update(tag)
    
    def delete_tag_by_id(self, tag_id: int) -> None:
        return self._delete(tag_id)
    
    def get_all_tags(self) -> List[Tag]:
        return self._get_all()
    
    def get_tag_by_name(self, value: str) -> Tag:
        return self._search_one_with("name", value)