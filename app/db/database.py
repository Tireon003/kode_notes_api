from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.db.config import setting
from sqlalchemy import URL


url_obj = URL.create(
    drivername="postgresql+asyncpg",
    username=setting.DB_USER,
    password=setting.DB_PASSWORD,
    host=setting.DB_HOST,
    port=setting.DB_PORT,
    database=setting.DB_NAME,
)

async_engine = create_async_engine(
    url=url_obj,
    # url=setting.db_async_url,
    echo=True
)

async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)


@asynccontextmanager
async def async_session():
    try:
        async with async_session_maker() as session:
            yield session
    except Exception as e:
        print("Error in async_session:", e)
        await session.rollback()
        raise
    finally:
        await session.close()
