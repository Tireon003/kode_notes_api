from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, text, ForeignKey
from typing import Annotated
from datetime import datetime


# Custom type hints
int_pk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):

    def __repr__(self):
        attrs = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"<{self.__class__.__name__}: {", ".join(attrs)}>"


class UserTable(Base):
    __tablename__ = 'users'

    user_id: Mapped[int_pk]
    user_name: Mapped[str] = mapped_column(String(30), unique=True)
    user_hashed_password: Mapped[str]

    user_notes: Mapped[list["NoteTable"]] = relationship(back_populates="from_user")


class NoteTable(Base):
    __tablename__ = 'notes'

    note_id: Mapped[int_pk]
    note_title: Mapped[str] = mapped_column(String(50))
    note_content: Mapped[str | None] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    by_user: Mapped[int] = mapped_column(ForeignKey('users.user_id'))

    from_user: Mapped["UserTable"] = relationship(back_populates="user_notes")
