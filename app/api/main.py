import uvicorn
from fastapi import FastAPI, Body, Depends, Response
from typing import Annotated
from app.db.orm import select_notes_by_user, insert_note, insert_new_user, select_user
from app.api.services import AuthService
from app.api.models import Note, UserDataDB, RegisterData
from app.api.dependencies import verify_user, verify_token, spell_note

app = FastAPI()


@app.post("/signup")
async def sign_up_user(register_data: Annotated[RegisterData, Body()]):
    user_in_db = await select_user(register_data.username)
    if user_in_db:
        return {"message": "username exists"}
    await insert_new_user(register_data)
    return {"message": "user created"}


@app.post("/login")
async def log_in_user(user_data: Annotated[UserDataDB, Depends(verify_user)], response: Response):
    token = AuthService.create_token(
        data={
            "id": user_data.user_id,
            "usr": user_data.user_name,
        }
    )
    response.set_cookie(key="access_token", value=token, secure=True, httponly=True)
    return {"access_token": token, "token_type": "Bearer"}


@app.post("/add_note")
async def add_note(note_data: Annotated[Note, Depends(spell_note)], by_user: Annotated[int, Depends(verify_token)]):
    await insert_note(by_user, note_data)
    return {"message": "note added", "note": note_data}


@app.get("/notes")
async def get_user_notes(by_user: Annotated[int, Depends(verify_token)]):
    notes = await select_notes_by_user(by_user)
    return notes


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000)
