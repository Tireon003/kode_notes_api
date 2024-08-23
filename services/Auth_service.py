import jwt
import datetime as dt
from fastapi import HTTPException


class AuthService:

    ALG = 'HS256'
    SECRET = "BI1i21b3b09kn9dcb78e2nTe23Frf411Vv7dmg12lht5e"

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
