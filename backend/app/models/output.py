from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class Output(Base):
    __tablename__ = 'outputs'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    storage_id = Column(Integer, ForeignKey('storage.id'), nullable=False)

    storage = relationship("Storage", back_populates="outputs")