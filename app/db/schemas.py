"""
Now not using schemas
"""


from pydantic import BaseModel, Field
from typing import Annotated
import datetime as dt


class Credentials(BaseModel):
    username: str = Field(max_length=30)
    password: str


class SignupUser(Credentials):
    class Config:
        orm_mode = True


class LoginUser(Credentials):

    class Config:
        orm_mode = True


class Note(BaseModel):
    title: str = Field(max_length=50)
    content: str | None = None


class NoteFromUser(Note):

    class Config:
        orm_mode = True


class NoteFromDB(Note):
    note_id: int
    created_at: Annotated[dt.datetime, ]

    class Config:
        orm_mode = True



