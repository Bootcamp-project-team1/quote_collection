from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

# 공통
class QuoteBase(BaseModel):
    content: str
    page: str
    book_id: Optional[int] = None
    user_id: int

# 문장 등록
class QuoteCreate(QuoteBase):
    pass

# 문장 수정
class QuoteUpdate(BaseModel):
    content: Optional[str] = None
    page: Optional[int] = None
    book_id: Optional[int] = None

# DB에서 관리되는 모델
class QuoteInDB(QuoteBase):
    quote_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

#클라이언트에게 반환할 모델 -> QuoteInDB 그대로
class QuoteRead(QuoteInDB):
    pass
