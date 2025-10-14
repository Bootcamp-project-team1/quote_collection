from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional, Dict, Any

class SourceBase(BaseModel):
    title: str
    source_type: str
    creator: str
    producer_id: Optional[int] = None
    publisher_id: Optional[int] = None
    release_year: Optional[int] = None
    isbn: Optional[str] = None

class SourceCreate(SourceBase):
    pass

class SourceUpdate(BaseModel):
    data: Optional[Dict[str, Any]] = None

class SourceInDB(SourceBase):
    id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class SourceRead(SourceInDB):
    pass
