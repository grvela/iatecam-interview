from sqlalchemy.orm import Session
from app.models.product import Product as ProductModel
from app.repositories.main import AbstractRepository
from app.schemas.product import Product, CreateProduct, UpdateProduct

from typing import List

class ProductRepository(AbstractRepository[ProductModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = ProductModel

    def create_product(self, product: CreateProduct) -> Product:
        return self._create(product)

    def get_product_by_id(self, product_id: int) -> Product:
        return self._get(product_id)

    def update_product(self, product: UpdateProduct) -> Product:
        return self._update(product)

    def delete_product_by_id(self, product_id: int) -> None:
        return self._delete(product_id)

    def get_all_products(self) -> List[Product]:
        return self._get_all()
    
    def get_product_by_name(self, value: str) -> Product:
        return self._search_one_with("name", value)
