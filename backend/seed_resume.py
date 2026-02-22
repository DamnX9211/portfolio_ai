from app.database import SessionLocal
from app.models.about import About
from app.models.education import Education
from app.models.experience import Experience
from app.models.skill import Skill
from app.models.project import Project

db = SessionLocal()

def seed_about():
    about = About(
        name="Rohit Kumar",
        headline="Backend Engineer | Python | Node.js | AI Systems",
        summary="Final year B.Tech student building scalable backend systems and AI-powered applications. Experienced in API design, databases, and production-ready software development."

    )
    db.add(about)

def seed_project():
    projects = [
        Project(
            title="AI Mock Interview System",
            description="AI-powered interview simulator that generates technical questions and evaluates responses.",
            tech_stack="React, Node.js, OpenAI API",
            github_url="https://github.com/DamnX9211",
            live_url=None
        ),
        Project(
            title="Car Rental Platform",
            description="Full stack car rental platform with booking system and authentication.",
            tech_stack="React, Express, MongoDB",
            github_url="https://github.com/DamnX9211",
            live_url=None
        ),
        Project(
            title="Data Alchemist",
            description="Platform for validating datasets and generating analytics insights.",
            tech_stack="Python, FastAPI, PostgreSQL",
            github_url="https://github.com/DamnX9211",
            live_url=None
        )
    ]
    db.add_all(projects)

def seed_experience():
    experience = Experience(
        company="Labmentix",
        role="Data Science & AI Intern",
        description="Built customer churn prediction model and deployed ML system for real-time predictions.",
        start_date=None,
        end_date=None
    )
    db.add(experience)

def seed_skills():
    skills = [
        Skill(category="Backend", name="Python"),
        Skill(category="Backend", name="Node.js"),
        Skill(category="Backend", name="Express"),
        Skill(category="Backend", name="FastAPI"),
        Skill(category="Frontend", name="React"),
        Skill(category="Database", name="PostgreSQL"),
        Skill(category="Database", name="MongoDB"),
        Skill(category="Tools", name="Docker"),
        Skill(category="Tools", name="Git")
    ]
    db.add_all(skills)

def seed_education():
        education = Education(
        institution="National Institute of Technology Durgapur",
        degree="B.Tech",
        field="Biotechnology",
        start_year=2022,
        end_year=2026
    )
        db.add(education)

def run_seed():
     seed_about()
     seed_project()
     seed_experience()
     seed_skills()
     seed_education()
     db.commit()
     print("Database seeded successfully.")

if __name__ == "__main__":
     run_seed()     
