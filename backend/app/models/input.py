from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class Input(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    storage_id = Column(Integer, ForeignKey('storage.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    storage = relationship("Storage", back_populates="inputs")
    user = relationship("User", back_populates="inputs")