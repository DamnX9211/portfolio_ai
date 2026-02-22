from pydantic import BaseModel
from uuid import UUID

class Aboutresponse(BaseModel):
    id: UUID
    name: str
    headline: str
    summary: str

    class Config:
        from_attributes = True