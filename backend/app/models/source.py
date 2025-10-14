from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, JSON
from sqlalchemy import func
from app.database import Base

class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    source_type = Column(Enum("book", "movie", "tv", "speech", "other", name="source_type"), nullable=False)
    creator = Column(String(255), nullable=False)
    pd_id = Column(Integer, ForeignKey("producers.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
