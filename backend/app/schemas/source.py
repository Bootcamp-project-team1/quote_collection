from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional, Dict, Any, Literal

class SourceBase(BaseModel):
    source_type: Literal['book', 'movie', 'drama', 'other']
    pd_id: int
    data: Dict[str, Any]

class SourceCreate(SourceBase):
    pass

class SourceUpdate(BaseModel):
    data: Optional[Dict[str, Any]] = None

class SourceInDB(SourceBase):
    source_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class SourceRead(SourceInDB):
    pass
