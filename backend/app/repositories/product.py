from sqlalchemy.orm import Session
from app.models.product import Product as ProductModel
from app.repositories.main import AbstractRepository
from app.schemas.product import Product, CreateProduct, UpdateProduct

class ProductRepository(AbstractRepository[ProductModel]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = ProductModel

    def create_product(self, product_data: CreateProduct) -> Product:
        product = ProductModel(
            name=product_data.name,
            tag_id=product_data.tag_id
        )
        return self._create(product)

    def get_product_by_id(self, product_id: int) -> Product:
        return self._get(product_id)

    def update_product(self, product_data: UpdateProduct) -> Product:
        return self._update(product_data)

    def delete_product(self, product_id: int):
        return self._delete(product_id)

    def get_all_products(self):
        return self._get_all()

    def search_products_by_field(self, field_name, value):
        return self._search_all_with(field_name, value)

    def search_product_by_field(self, field_name, value) -> Product:
        return self._search_one_with(field_name, value)
