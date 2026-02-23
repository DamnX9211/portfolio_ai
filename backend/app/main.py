from fastapi import FastAPI
from app.database import Base, engine
from app.models import about, education, experience, skill, project
from app.routes import resume_routes
from app.routes import chat_routes
from fastapi.middleware.cors import CORSMiddleware
from seed_resume import run_seed

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(resume_routes.router, prefix="/api")
app.include_router(chat_routes.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Portfolio Ai Backend Running"}

run_seed()
