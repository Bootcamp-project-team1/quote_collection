from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy import func
from app.database import Base
import enum

# 제작자 종류
class ProducerType(str, enum.Enum):
    publisher = "publisher"
    studio = "studio"
    broadcast = "broadcast"
    other = "other"

class Producer(Base):
    __tablename__ = "producers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    pd_type = Column(Enum(ProducerType, name="pd_type"), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
