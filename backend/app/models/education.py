from sqlalchemy import Column, Integer, String
from app.database import Base

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    field = Column(String, nullable=False)
    start_year = Column(Integer)
    end_year = Column(Integer)