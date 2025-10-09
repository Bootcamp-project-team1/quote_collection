from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class QuoteTag(Base):
    __tablename__ = "quote_tags"

    quote_id = Column(Integer, ForeignKey("quotes.id", ondelete="CASCADE"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
