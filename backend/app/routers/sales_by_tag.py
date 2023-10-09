from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.sales_by_tag import SalesByTagService
from app.schemas.sales_by_tag import SalesByTag

from typing import List

router = APIRouter(
    prefix="/sales_by_tag",
    tags=["Sales by tag"]
)

@router.get("/", response_model=List[SalesByTag])
def get_sales_by_tag(db: Session = Depends(get_db)) -> List[SalesByTag]:
    return SalesByTagService(db).get_sales_by_tag()
