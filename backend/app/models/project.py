from sqlalchemy import Column, Integer, String, text
from app.database import Base

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tech_stack = Column(String)
    github_url = Column(String)
    live_url = Column(String)