from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Setting(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_HOST_ALEMBIC: str

    @property
    def db_async_url(self) -> str:
        print(f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}'
               f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}' \
               f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


    @property
    def db_async_url_migrations(self) -> str:
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST_ALEMBIC}:{self.DB_PORT}/{self.DB_NAME}")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


setting = Setting()
