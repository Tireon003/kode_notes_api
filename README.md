## Test task by Kode

### Description
It is a simple app with API and Postres implementation.
API based on FastAPI. Functionality:
 - Sign up
 - Log in
 - Add new note
 - Show notes list

API interacts with DB on Postres.
API has an authorization and authentication system based on JWT.
Each note spelling before add to DB. Thus, notes haven't mistakes in it's title and content parts.

### How to build and run?

#### Build:
```commandline
docker-compose build
```

#### Run:
```commandline
docker-compose up
```

#### Stop:
```commandline
docker-compose down
```
