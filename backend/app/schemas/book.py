from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    publisher: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None

class BookInDB(BookBase):
    book_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class BookRead(BookInDB):
    pass
