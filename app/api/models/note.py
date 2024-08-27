from pydantic import BaseModel, Field
from datetime import datetime


class Note(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    content: str | None = Field(min_length=1, max_length=500, default=None)


class NoteFromDB(Note):
    note_id: int
    by_user: int
    created_at: datetime
