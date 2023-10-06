from app.config.session import AppService

from app.schemas.tag import CreateTag, Tag

from app.repositories.tag import TagRepository

from typing import List

class TagService(AppService):
    def create_tag(self, tag: CreateTag) -> Tag:
        db_tag = TagRepository(self.db).create_tag(tag)
        return db_tag
    
    def get_tag(self, tag_id: int) -> Tag:
        return TagRepository(self.db).get_tag(tag_id=tag_id)

    #TODO - FIX Bussiness Logic    
    def update_tag(self, tag: Tag) -> Tag:
        db_tag = self.get_tag(tag.id)

        if db_tag:
            db_tag.name = tag.name
            return TagRepository(self.db).update_tag(db_tag)
        else:
            return None
    
    def get_all_tags(self) -> List[Tag]:
        return TagRepository(self.db).get_all_tags()