from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.product import ProductService
from app.schemas.product import Product, CreateProduct, UpdateProduct
from typing import List

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=Product)
def create_product(product_data: CreateProduct, db: Session = Depends(get_db)):
    return ProductService(db).create_product(product_data)

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService(db).get_product(product_id)

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: UpdateProduct, db: Session = Depends(get_db)):
    return ProductService(db).update_product(product_id, product_data)

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService(db).delete_product(product_id)

@router.get("/", response_model=List[Product])
def read_all_products(db: Session = Depends(get_db)):
    return ProductService(db).get_all_products()
