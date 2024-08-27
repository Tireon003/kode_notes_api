import jwt
import datetime as dt
from fastapi import HTTPException
from dotenv import load_dotenv
import os
import bcrypt


load_dotenv()


class AuthService:

    ALG = 'HS256'
    SECRET = os.getenv("SECRET")

    @classmethod
    def create_token(cls, data: dict) -> str:
        data_copy = data.copy()
        data_copy["exp"] = dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=7)
        return jwt.encode(payload=data_copy, key=cls.SECRET, algorithm=cls.ALG)

    @classmethod
    def read_token(cls, token: str) -> dict | str:
        try:
            decoded_token = jwt.decode(token, cls.SECRET, algorithms=[cls.ALG])
            exp_time = dt.datetime.fromtimestamp(decoded_token["exp"], dt.timezone.utc)
            if exp_time < dt.datetime.now(dt.timezone.utc):
                raise jwt.ExpiredSignatureError()
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Token is expired",
                headers={"WWW-Authenticate": "Bearer"}
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"}
            )

    @staticmethod
    def hash_pwd(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('ascii')

    @staticmethod
    def check_pwd(stored_password: str, provided_password: str) -> bool:
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('ascii'))