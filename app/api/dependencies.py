from typing import Annotated
from fastapi import HTTPException, Body, status, Depends
from fastapi.security import OAuth2PasswordBearer
from configs import data
from models import LoginData, Note
from services import PostgresDB, AuthService
from services import Speller

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def verify_user(login_data: Annotated[LoginData, Body()]):
    db = PostgresDB(**data)
    user_data_record = await db.get_user(login_data.username)
    try:
        user_data = LoginData(
            **{
                "username": user_data_record["user_name"],
                "password": user_data_record["user_pwd"],
            }
        )
        if user_data.password == login_data.password:
            return user_data
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except TypeError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such user exists",
            headers={"WWW-Authenticate": "Bearer"}
        )


async def verify_token(access_token: Annotated[str, Depends(oauth2_scheme)]):
    payload = AuthService.read_token(access_token)
    return payload["usr"]


async def spell_note(note_data: Annotated[dict, Body()]) -> Note:
    note_data["title"] = Speller.correct_text(note_data["title"])
    if note_data.get("content"):
        note_data["content"] = Speller.correct_text(note_data["content"])
    return Note(**note_data)
