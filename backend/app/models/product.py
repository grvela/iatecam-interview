from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), nullable=False)

    tag = relationship("Tag", back_populates="products")