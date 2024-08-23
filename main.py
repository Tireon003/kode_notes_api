import uvicorn
from fastapi import FastAPI


if __name__ == '__main__':
    app = FastAPI()
    uvicorn.run(app)
    