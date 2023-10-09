from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.sales_by_product import SalesByProductService

from app.schemas.sales_by_product import SalesByProduct
from typing import List

from app.schemas.sales_by_tag import SalesByTag

from app.services.sales_by_tag import SalesByTagService

from app.middlewares.auth import get_current_user

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/sales/by/product", response_model=List[SalesByProduct])
def get_sales_by_product(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) -> List[SalesByProduct]:
    return SalesByProductService(db).get_sales_by_product()

@router.get("/sales/by/tag", response_model=List[SalesByTag])
def get_sales_by_tag(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)) -> List[SalesByTag]:
    return SalesByTagService(db).get_sales_by_tag()
