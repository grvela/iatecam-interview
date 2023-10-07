from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from sqlalchemy.orm import relationship

from app.config.database import Base

class Input(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    storage_id = Column(Integer, ForeignKey('storages.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    storage = relationship("Storage", back_populates="inputs")
    user = relationship("User", back_populates="inputs")