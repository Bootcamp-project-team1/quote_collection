from sqlalchemy import Column, Integer, String, DateTime, TEXT, ForeignKey ### 외래키 추가 ###
from sqlalchemy import func
from app.database import Base  
from sqlalchemy.orm import relationship


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False)
    content = Column(TEXT, nullable=False)
    page = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    tags = relationship("Tag", secondary="quote_tags", back_populates="quotes")

    ### Movie와의 관계 설정###
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", back_populates="quotes")