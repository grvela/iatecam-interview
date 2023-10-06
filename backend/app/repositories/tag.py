from app.schemas.tag import CreateTag, Tag
from app.models.tag import Tag as TagModel
from app.repositories.main import AbstractRepository

from sqlalchemy.orm import Session

from typing import List


class TagRepository(AbstractRepository[TagModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = TagModel

    def create_tag(self, tag: CreateTag):
        tag_obj = TagModel(name=tag.name)
        return self._create(tag_obj)

    def get_tag(self, tag_id: int) -> Tag:
        return self._get(tag_id)
    
    def update_tag(self, tag: Tag) -> Tag:
        return self._update(tag)
    
    def get_all_tags(self) -> List[Tag]:
        return self._get_all()
    
    def get_by_name(self, tag_name: str) -> Tag:
        return self._search_one_with(field_name="name", value=tag_name)