from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.tag import CreateTag, Tag
from app.services.tag import TagService

router = APIRouter(
    prefix="/tag"
)

@router.post("/")
def create_tag(tag: CreateTag, db: Session = Depends(get_db)) -> Tag:
    result = TagService(db).create_tag(tag=tag)
    return result