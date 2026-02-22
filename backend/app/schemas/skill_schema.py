from pydantic import BaseModel
from uuid import UUID

class SkillResponse(BaseModel):
    id: UUID
    name: str
    category: str

    class Config:
        from_attributes = True