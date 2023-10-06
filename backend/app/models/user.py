from sqlalchemy import Column, Integer, String, Enum

from app.config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    username= Column(String, unique=True)
    password = Column(String)