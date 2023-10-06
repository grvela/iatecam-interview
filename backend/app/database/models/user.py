from sqlalchemy import Column, Integer, String

from app.database.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    username= Column(String, unique=True)
    password = Column(String)
    role= Column(String)