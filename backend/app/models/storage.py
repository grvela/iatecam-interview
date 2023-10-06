from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.config.database import Base

class Storage(Base):
    __tablename__ = 'storage'

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    product = relationship("Product", back_populates="storage")
    user = relationship("User", back_populates="inputs")