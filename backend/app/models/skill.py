from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Skill(Base):
    __tablename__ = "skills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)