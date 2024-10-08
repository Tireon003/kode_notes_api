from app.api.models import Note, RegisterData
from app.db.database import async_session
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.db.models import NoteTable, UserTable
from app.api.services import AuthService
import asyncio


async def select_notes_by_user(user_id: int) -> list:
    async with async_session() as session:
        # query = select(NoteTable).filter_by(by_user=user_id)
        # result = await session.execute(query)
        # notes_list = [dict(item) for item in result.scalars().all()]
        # print(notes_list)
        # return notes_list
        query = select(UserTable).options(joinedload(UserTable.user_notes)).filter_by(user_id=user_id)
        user = await session.scalar(query)
        user_notes = user.user_notes
        return user_notes


async def select_user(username: str) -> dict | None:
    async with async_session() as session:
        query = select(UserTable).filter_by(user_name=username)
        user = await session.scalar(query)
        print(user)
        if not user:
            return
        else:
            return {
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_hashed_password": user.user_hashed_password,
            }


async def insert_note(userid: int, note: Note):
    async with async_session() as session:
        new_note = NoteTable(
            note_title=note.title,
            note_content=note.content,
            by_user=userid
        )
        session.add(new_note)
        await session.commit()


async def insert_new_user(credentials: RegisterData):
    async with async_session() as session:
        new_user = UserTable(
            user_name=credentials.username,
            user_hashed_password=AuthService.hash_pwd(credentials.password)
        )
        session.add(new_user)
        await session.commit()

