from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Education(Base):
    __tablename__ = "education"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    institution = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    field = Column(String, nullable=False)
    start_year = Column(Integer)
    end_year = Column(Integer)