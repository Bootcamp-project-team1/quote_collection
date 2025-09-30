from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

quote_tags = Table(
    "quote_tags",
    Base.metadata,
    Column("quote_id", Integer, ForeignKey("quotes.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)
