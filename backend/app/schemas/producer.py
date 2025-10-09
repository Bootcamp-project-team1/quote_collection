from pydantic import BaseModel, Field
from datetime import datetime, timezone

class ProducerBase(BaseModel):
    name: str
    pd_type: str  # 예: "book", "movie", "drama"

class ProducerCreate(ProducerBase):
    pass

class ProducerUpdate(BaseModel):
    name: str | None = None
    pd_type: str | None = None

class ProducerInDB(ProducerBase):
    producer_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class ProducerRead(ProducerInDB):
    pass
