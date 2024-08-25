from dotenv import load_dotenv
from os import environ

load_dotenv()

data = {
    "user": environ["POSTGRES_DB_USER"],
    "password": environ["POSTGRES_DB_PASSWORD"],
    "database": "database",
    "host": "db",
}
