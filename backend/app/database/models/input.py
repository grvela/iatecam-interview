from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.config import Base

class Input(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    storage_id = Column(Integer, ForeignKey('storage.id'), nullable=False)

    storage = relationship("Storage", back_populates="inputs")