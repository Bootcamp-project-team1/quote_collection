from pydantic import BaseModel, Field
from datetime import datetime, timezone

class LikeBase(BaseModel):
    user_id: int
    quote_id: int

class LikeCreate(LikeBase):
    pass

class LikeInDB(LikeBase):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class LikeRead(LikeInDB):
    pass
