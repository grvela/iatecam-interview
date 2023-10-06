from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.tag import CreateTag, Tag
from app.services.tag import TagService

from typing import List

router = APIRouter(
    prefix="/tag"
)

@router.post("/")
def create_tag(tag: CreateTag, db: Session = Depends(get_db)) -> Tag:
    result = TagService(db).create_tag(tag=tag)
    return result

@router.get("/{item_id}")
def get_tag(tag_id: int, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).get_tag(tag_id)

@router.put("/")
def update_tag(tag: Tag, db: Session = Depends(get_db)) -> Tag:
    try:
        tag_updated = TagService(db).update_tag(tag)
        return tag_updated
    except:
        print("Deu erro")

@router.get("/")
def get_all_tags(db: Session = Depends(get_db)) -> List[Tag]:
    return TagService(db).get_all_tags()