from app.schemas.tag import CreateTag
from app.models.tag import Tag
from app.repositories.base import AbstractRepository


class TagRepository(AbstractRepository[Tag]):

    def create_with_class(self, tag: CreateTag) -> Tag:
        db_tag = Tag(name=tag.name)
        return self.create(db_tag)

    def create_tag(self, tag: CreateTag) -> Tag:
        db_tag = Tag(name=tag.name)
        self.db.add(db_tag)
        self.db.commit()
        self.db.refresh(db_tag)
        return db_tag