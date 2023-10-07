from fastapi import HTTPException, Response

from app.config.session import AppService

from app.schemas.tag import Tag, CreateTag, UpdateTag

from app.repositories.tag import TagRepository

from typing import List

class TagService(AppService):
    def create_tag(self, tag: CreateTag) -> Tag:
        db_tag = TagRepository(self.db).get_by_name(tag_name=tag.name)

        if db_tag:
            return db_tag

        return TagRepository(self.db).create_tag(tag)
    
    def get_tag(self, tag_id: int) -> Tag:
        db_tag = TagRepository(self.db).get_tag(tag_id=tag_id)

        if not db_tag:
            raise HTTPException(status_code=404, detail="Tag not found")

        return db_tag

    def update_tag(self, item_id: int, tag: UpdateTag) -> Tag:
        db_tag = self.get_tag(item_id)

        existing_tag = TagRepository(self.db).get_by_name(tag_name=tag.name)
        
        if existing_tag:
            raise HTTPException(status_code=409, detail="Tag is already exists")

        db_tag.name = tag.name
        return TagRepository(self.db).update_tag(db_tag)
    
    def delete_tag(self, item_id: int):
        db_tag = self.get_tag(item_id)

        TagRepository(self.db).delete_tag(db_tag.id)

        existing_tag = TagRepository(self.db).get_tag(tag_id=item_id)

        if existing_tag:
            raise HTTPException(status_code= 400, detail="Can't delete tag")
        
        return Response(status_code=204)
              
    def get_all_tags(self) -> List[Tag]:
        return TagRepository(self.db).get_all_tags()
    
    def get_tag_by_name(self, name: str) -> Tag:
        return TagRepository(self.db).get_by_name(name)