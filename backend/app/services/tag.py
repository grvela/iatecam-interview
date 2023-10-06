from app.config.session import AppService

from app.schemas.tag import CreateTag, Tag

from app.repositories.tag import TagRepository

class TagService(AppService):
    def create_tag(self, tag: CreateTag) -> Tag:
        db_tag = TagRepository(self.db).create_with_class(tag=tag)
        return db_tag