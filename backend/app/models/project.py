from sqlalchemy import Column, Integer, String, text
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tech_stack = Column(String)
    github_url = Column(String)
    live_url = Column(String)