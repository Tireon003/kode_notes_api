from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import setting

async_engine = create_async_engine(
    url=setting.db_async_url,
    echo=True
)

async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)


@asynccontextmanager
async def async_session():
    async with async_session_maker() as session:
        yield session
