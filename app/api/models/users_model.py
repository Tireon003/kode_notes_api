from pydantic import BaseModel, Field


class LoginData(BaseModel):
    username: str = Field(min_length=8, max_length=30)
    password: str


class UserDataDB(LoginData):
    id: int


class RegisterData(LoginData):
    pass
