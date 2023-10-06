from sqlalchemy import Column, String, Integer

from app.database.config import Base

class Tag(Base):
    __tablename__ = "tags"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False, unique=True)