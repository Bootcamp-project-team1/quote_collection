from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy import func
from app.database import Base

class Bookmark(Base):
    __tablename__ = "bookmarks"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    quote_id = Column(Integer, ForeignKey("quotes.id", ondelete="CASCADE"), primary_key=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    