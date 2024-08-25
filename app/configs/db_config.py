import os
from dotenv import load_dotenv

load_dotenv()

data = {
    "user": os.getenv("POSTGRES_DB_USER"),
    "password": os.getenv("POSTGRES_DB_PASSWORD"),
    "database": "kode_proj_db",
    "host": "localhost",
}
