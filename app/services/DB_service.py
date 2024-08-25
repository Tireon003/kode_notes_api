import asyncpg
from contextlib import asynccontextmanager
from app.models import Note, LoginData


class PostgresDB:
    def __init__(self, user: str, password: str, database, host: str = 'localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host

    @asynccontextmanager
    async def connection(self):
        conn = await asyncpg.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host
        )
        yield conn
        await conn.close()

    async def add_user(self, signup_data: LoginData):
        async with self.connection() as conn:
            result = await conn.execute(
                "INSERT INTO users (user_name, user_pwd) VALUES ($1, $2)",
                signup_data.username, signup_data.password
            )
            return result

    async def get_user(self, username: str):
        async with self.connection() as conn:
            result = await conn.fetchrow("SELECT * FROM users WHERE user_name = $1", username)
            return result

    async def add_note(self, note: Note, username: str):
        async with self.connection() as conn:
            result = await conn.execute(
                "INSERT INTO notes (by_user, note_title, note_content, created_at) VALUES ($1, $2, $3, $4)",
                username, note.title, note.content, note.created_at
            )
            return result

    async def get_notes(self, user_name: str):
        async with self.connection() as conn:
            result = await conn.fetch("SELECT * FROM notes WHERE by_user = $1", user_name)
            return result
