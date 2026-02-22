from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.ai_service import generate_ai_response
from app.schemas.chat_schema import ChatRequest

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    answer = await generate_ai_response(request.question, db)

    return {"answer": answer}