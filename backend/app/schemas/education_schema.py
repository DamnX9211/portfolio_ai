from pydantic import BaseModel
from uuid import UUID

class EducationResponse(BaseModel):
    id: UUID
    institution: str
    degree: str
    field: str
    start_year: int | None
    end_year: int | None

    class Config:
        from_attributes = True