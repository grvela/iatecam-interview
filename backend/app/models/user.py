from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    username= Column(String, unique=True)
    password = Column(String)

    storages = relationship('Storage', back_populates='user')
    inputs = relationship('Input', back_populates='user')
    outputs = relationship('Output', back_populates='user')