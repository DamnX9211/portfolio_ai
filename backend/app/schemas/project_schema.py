from pydantic import BaseModel
from uuid import UUID

class ProjectResponse(BaseModel):
    id: UUID
    title: str
    description: str 
    tech_stack: str | None
    github_url: str | None
    live_url: str | None

    class Config:
        from_attributes = True