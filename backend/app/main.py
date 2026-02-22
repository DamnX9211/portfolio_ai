from fastapi import FastAPI
from app.database import Base, engine
from app.models import about, education, experience, skill, project
from app.routes import resume_routes
from app.routes import chat_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(resume_routes.router, prefix="/api")
app.include_router(chat_routes.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Portfolio Ai Backend Running"}

