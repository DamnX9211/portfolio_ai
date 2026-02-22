from sqlalchemy import Column, Integer, String, Text, Date
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Experience(Base):
    __tablename__ = "experience"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text, nullable=False)