from fastapi import APIRouter, Depends, HTTPException

from starlette.responses import Response

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.tag import Tag, CreateTag, UpdateTag
from app.services.tag import TagService

from app.middlewares.auth import get_current_user

from typing import List

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)

@router.post("/")
def create_tag(tag: CreateTag, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).create_tag(tag=tag)

@router.get("/{item_id}")
def get_tag(tag_id: int, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).get_tag_by_id(tag_id)

@router.put("/{item_id}")
def update_tag(item_id: int, tag: UpdateTag, db: Session = Depends(get_db)) -> Tag:
    return TagService(db).update_tag_by_id(item_id, tag)

@router.delete("/{item_id}")
def delete_tag(item_id: int, db: Session = Depends(get_db)):
    return TagService(db).delete_tag_by_id(item_id)

@router.get("/")
def get_all_tags(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) -> List[Tag]:
    return TagService(db).get_all_tags()