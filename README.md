## Test task by Kode

### Description
It is a simple app with API and Postgres implementation.
API based on FastAPI. Functionality:
 - Sign up
 - Log in
 - Add new note
 - Show notes list

API interacts with DB on Postgres by SQLAlchemy ORM.
Implemented Alembic migrations.
API has an authorization and authentication system based on JWT.
Passwords are secured by encryption and hashed storing in DB.
Each note spelling before add to DB. Thus, notes haven't mistakes in its title and content parts.

### Stack
 - FastAPI
 - SQLAlchemy ORM
 - Alembic
 - Docker & docker-compose


### How to build and run?

#### Build:
```commandline
docker-compose build
```

#### Run (background):
```commandline
docker-compose up -d
```

#### Stop:
```commandline
docker-compose stop
```


## Tests

You can test API in Postman using Postman collections. JSON-collection in project directory.