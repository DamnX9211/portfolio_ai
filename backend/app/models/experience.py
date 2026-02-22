from sqlalchemy import Column, Integer, String, Text, Date
from app.database import Base

class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text, nullable=False)