from sqlalchemy import Column, Integer, String, Text
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class About(Base):
    __tablename__ = "about"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    headline = Column(String, nullable=False)
    summary = Column(Text, nullable=False)