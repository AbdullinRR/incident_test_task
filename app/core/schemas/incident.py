from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IncidentBase(BaseModel):
    text: str
    status: Optional[str] = "open"
    source: str

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdate(BaseModel):
    status: str

class IncidentResponse(IncidentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True