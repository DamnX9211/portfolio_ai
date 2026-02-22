from sqlalchemy.orm import Session
from app.models.about import About
from app.models.education import Education
from app.models.experience import Experience
from app.models.skill import Skill
from app.models.project import Project


def get_resume_data(db: Session):
    about = db.query(About).first()
    projects = db.query(Project).all()
    experience = db.query(Experience).all()
    education = db.query(Education).all()
    skills = db.query(Skill).all()

    return {
        "about": about,
        "projects": projects,
        "experience": experience,
        "education": education,
        "skills": skills,
    
    }