from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from app.database import Base


class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())