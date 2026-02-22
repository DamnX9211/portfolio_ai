from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.resume_service import get_resume_data

router = APIRouter()

@router.get("/resume")
def get_resume(db: Session = Depends(get_db)):
    return get_resume_data(db)