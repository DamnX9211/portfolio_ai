from pydantic import BaseModel
from uuid import UUID
from datetime import date

class ExperienceResponse(BaseModel):
    id: UUID
    company: str
    role: str
    description: str
    start_date: date | None
    end_date: date | None

    class Config:
        from_attributes = True