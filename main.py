import uvicorn
from fastapi import FastAPI, Body, Depends, Response
from typing import Annotated
from services import AuthService, PostgresDB
from models import Note, LoginData
from dependencies import verify_user, verify_token, spell_note
from configs import data

app = FastAPI()


@app.post("/signup")
async def sign_up_user(login_data: Annotated[LoginData, Body()]):
    db = PostgresDB(**data)
    await db.add_user(login_data)
    return {"message": "user created"}


@app.post("/login")
async def log_in_user(login_data: Annotated[LoginData, Depends(verify_user)], response: Response):
    token = AuthService.create_token(
        data={
            "usr": login_data.username,
        }
    )
    response.set_cookie(key="access_token", value=token, secure=True, httponly=True)
    return {"access_token": token}


@app.post("/add_note")
async def add_note(note_data: Annotated[Note, Depends(spell_note)], by_user: Annotated[str, Depends(verify_token)]):
    db = PostgresDB(**data)
    await db.add_note(note=note_data, username=by_user)
    return {"message": "note added", "note": note_data}


@app.get("/notes")
async def get_user_notes(by_user: Annotated[str, Depends(verify_token)]):
    db = PostgresDB(**data)
    notes = await db.get_notes(user_name=by_user)
    return notes


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
