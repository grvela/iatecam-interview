from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.sales_by_product import SalesByProductService

from app.schemas.sales_by_product import SalesByProduct
from typing import List


router = APIRouter(
    prefix="/sales_by_product",
    tags=["Sales by product"]
)

@router.get("/", response_model=List[SalesByProduct])
def get_sales_by_product(db: Session = Depends(get_db)) -> List[SalesByProduct]:
    return SalesByProductService(db).get_sales_by_product()
