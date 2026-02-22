from fastapi import FastAPI
from app.database import Base, engine
from app.models import about, education, experience, skill, project

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Portfolio Ai Backend Running"}