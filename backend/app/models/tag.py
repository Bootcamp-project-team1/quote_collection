from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship ### 추가 ###
# from .quote_tag import quote_tags
from .movie import movie_tag_association ### 추가 ###

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    # quotes = relationship("Quote", secondary="quote_tags", back_populates="tags") ### 기존 "quote_tags" 문자열 대신 변수로 변경 ###
    quotes = relationship("Quote", secondary='quote_tags', back_populates="tags")

    ### Movie와의 다대다 관계 설정 ###
    movies = relationship(
        "Movie",
        secondary=movie_tag_association,
        back_populates="tags"
    )
