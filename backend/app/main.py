from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Portfolio Ai Backend Running"}