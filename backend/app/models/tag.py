from sqlalchemy import Column, Integer, String
from app.database import Base
from .quote_tag import quote_tags

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
