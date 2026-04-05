from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RecordBase(BaseModel):
    type: str
    amount: float
    category: str
    date: datetime
    notes: Optional[str] = None

class RecordUpdate(BaseModel):
    type: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[datetime] = None
    notes: Optional[str] = None

class RecordResponse(BaseModel):
    id: int
    user_id: int
    type: str
    amount: float
    category: str
    date: datetime
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True