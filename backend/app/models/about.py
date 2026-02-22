from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class About(Base):
    __tablename__ = "about"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    headline = Column(String, nullable=False)
    summary = Column(Text, nullable=False)