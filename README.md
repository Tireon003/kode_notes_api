## Test task by Kode

### Description
It is a simple app with API and Postres implementation.
API based on FastAPI. Functionality:
 - Sign up
 - Log in
 - Add new note
 - Show notes list

API interacts with DB on Postgres.
API has an authorization and authentication system based on JWT.
Each note spelling before add to DB. Thus, notes haven't mistakes in its title and content parts.

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
docker-compose down
```

***Important**

After building an app, you have to restore db in Postgres, using **notes_db_template.backup** dump file.

## Tests

You can test API in Postman using Postman collections. JSON-collection in project directory.