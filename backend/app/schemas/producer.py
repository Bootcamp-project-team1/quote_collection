from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Literal

class ProducerBase(BaseModel):
    name: str
    pd_type: Literal['book','movie','drama', 'other']

class ProducerCreate(ProducerBase):
    pass

class ProducerUpdate(BaseModel):
    name: str | None = None
    pd_type: Literal['book','movie','drama', 'other'] | None = None

class ProducerInDB(ProducerBase):
    producer_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class ProducerRead(ProducerInDB):
    pass
