from pydantic import BaseModel, Field


class LoginData(BaseModel):
    username: str = Field(min_length=8, max_length=30)
    password: str


class UserDataDB(BaseModel):
    user_id: int
    user_name: str = Field(min_length=8, max_length=30)
    user_hashed_password: str


class RegisterData(LoginData):
    pass
