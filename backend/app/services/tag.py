from fastapi import HTTPException, Response

from app.config.session import AppService

from app.schemas.tag import Tag, CreateTag, UpdateTag

from app.repositories.tag import TagRepository

from typing import List

class TagService(AppService):
    def create_tag(self, tag: CreateTag) -> Tag:
        tag_data = TagRepository(self.db).get_tag_by_name(tag.name)

        if tag_data:
            return tag_data

        return TagRepository(self.db).create_tag(tag)
    
    def get_tag_by_id(self, tag_id: int) -> Tag:
        tag_data = TagRepository(self.db).get_tag_by_id(tag_id)

        if not tag_data:
            raise HTTPException(status_code=404, detail="Tag not found")

        return tag_data

    def update_tag_by_id(self, tag_id: int, tag: UpdateTag) -> Tag:
        tag_data = self.get_tag_by_id(tag_id)

        existing_tag = TagRepository(self.db).get_tag_by_name(tag.name)
        
        if existing_tag:
            raise HTTPException(status_code=409, detail="Tag is already exists")

        tag_data.name = tag.name

        return TagRepository(self.db).update_tag(tag_data)
    
    def delete_tag_by_id(self, tag_id: int):
        tag_data = self.get_tag_by_id(tag_id)

        TagRepository(self.db).delete_tag_by_id(tag_data.id)

        existing_tag = TagRepository(self.db).get_tag_by_id(tag_data.id)

        if existing_tag:
            raise HTTPException(status_code= 400, detail="Can't delete tag")
        
        return Response(status_code=204)
              
    def get_all_tags(self) -> List[Tag]:
        return TagRepository(self.db).get_all_tags()