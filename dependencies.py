from typing import Annotated
from fastapi import HTTPException, Body, status, Depends
from fastapi.security import OAuth2PasswordBearer
from configs import data
from models import LoginData
from services import PostgresDB, AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def verify_user(login_data: Annotated[LoginData, Body()]):
    db = PostgresDB(**data)
    user_data_record = await db.get_user(login_data.username)
    user_data = LoginData(
        **{
            "username": user_data_record["user_name"],
            "password": user_data_record["user_pwd"],
        }
    )
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such user exists",
            headers={"WWW-Authenticate": "Bearer"}
        )
    else:
        if user_data.password == login_data.password:
            return user_data
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
                headers={"WWW-Authenticate": "Bearer"}
            )


async def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = AuthService.read_token(token)
    return payload["usr"]
