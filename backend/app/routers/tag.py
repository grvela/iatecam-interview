from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.tag import Tag, CreateTag, UpdateTag
from app.services.tag import TagService

from typing import List

router = APIRouter(
    prefix="/tag"
)

@router.post("/")
def create_tag(tag: CreateTag, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).create_tag(tag=tag)

@router.get("/{item_id}")
def get_tag(tag_id: int, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).get_tag(tag_id)

@router.put("/{item_id}")
def update_tag(item_id: int, tag: UpdateTag, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).update_tag(item_id, tag)

@router.get("/")
def get_all_tags(db: Session = Depends(get_db)) -> List[Tag]:
    return TagService(db).get_all_tags()