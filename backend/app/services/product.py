from fastapi import HTTPException
from app.schemas.product import Product, CreateProduct, UpdateProduct
from app.repositories.product import ProductRepository
from sqlalchemy.orm import Session
from typing import List

from app.services.tag import TagService
from app.config.session import AppService

class ProductService(AppService):
    def create_product(self, product_data: CreateProduct) -> Product:
       db_tag = TagService(self.db).create_tag(product_data.tag_name)
       db_product = ProductRepository(self.db).search_product_by_field(field_name="name", value=product_data.name)

       if db_product:
           if db_product.tag_id == db_tag.id:
               return db_product
        
       product_data.tag_id = db_tag.id
       return ProductRepository(self.db).create_product(product_data)

    def get_product(self, product_id: int) -> Product:
        db_product = ProductRepository(self.db).get_product_by_id(product_id)
        
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")

        return db_product

    def update_product(self, product_id: int, product_data: UpdateProduct) -> Product:
        db_product = self.get_product(product_id)
        
        return ProductRepository(self.db).update_product(product_id, product_data)

    def delete_product(self, product_id: int):
        db_product = self.get_product(product_id)
        
        ProductRepository(self.db).delete_product(db_product.id)
        
        existing_product = ProductRepository(self.db).get_product_by_id(product_id)
        
        if existing_product:
            raise HTTPException(status_code=400, detail="Can't delete product")

    def get_all_products(self) -> List[Product]:
        return ProductRepository(self.db).get_all_products()
    
    def get_product_by_field(self, field_name: str, value: str) -> Product:
        product_data = ProductRepository(self.db).search_product_by_field(field_name, value)

        if not product_data:
            raise HTTPException(status_code=404, detail="Product not found")
        
        return product_data
