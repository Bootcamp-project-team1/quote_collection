from sqlalchemy import Column, Integer, String, DateTime, TEXT
from sqlalchemy import func
from app.database import Base  
from sqlalchemy.orm import relationship


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=True)
    content = Column(TEXT, nullable=False)
    page = Column(String(255), nullable=False)
    likes_count = Column(Integer, nullable=False, server_default = "0")
    created_at = Column(DateTime, server_default=func.now())

    tags = relationship("Tag", secondary="quote_tags", back_populates="quotes")