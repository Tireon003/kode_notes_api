from typing import Annotated
from fastapi import HTTPException, Body, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.api.models import LoginData, Note, UserDataDB
from app.api.services import AuthService, Speller
from app.db.orm import select_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def verify_user(login_data: Annotated[LoginData, Depends(OAuth2PasswordRequestForm)]):
    valid_user_data = await select_user(login_data.username)
    if not valid_user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such user exists",
            headers={"WWW-Authenticate": "Bearer"}
        )
    elif not AuthService.check_pwd(valid_user_data["user_hashed_password"], login_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    else:
        user_data = UserDataDB(**valid_user_data)
        return user_data


async def verify_token(access_token: Annotated[str, Depends(oauth2_scheme)]):
    payload = AuthService.read_token(access_token)
    return payload["id"]


async def spell_note(note_data: Annotated[Note, Body()]) -> Note:
    note_data.title = Speller.correct_text(note_data.title)
    if note_data.content:
        note_data.content = Speller.correct_text(note_data.content)
    return note_data
