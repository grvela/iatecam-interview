from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from sqlalchemy.orm import relationship

from app.config.database import Base

class SalesByProduct(Base):
    __tablename__ = 'sales_by_product'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), index=True)
    amount = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="sales_by_product")