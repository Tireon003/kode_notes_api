from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Note(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    content: Optional[str] = Field(min_length=1, max_length=500, default=None)
    created_at: datetime = Field(default_factory=datetime.now)

