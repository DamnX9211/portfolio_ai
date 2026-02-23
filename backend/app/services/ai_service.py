import httpx
from sqlalchemy.orm import Session
from app.config import settings
from app.services.resume_service import get_resume_data

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def detect_section(question: str):
    q = question.lower()

    if "project" in q and ("explain" in q or "architecture" in q or "detail" in q):
        return "project_detail"
    
    if "project" in q:
        return "projects"
    
    if "skills" in q or "technology" in q:
        return "skills"
    
    if "experience" in q or "work" in q:
        return "experience"
    
    return "general"

async def generate_ai_response(question: str, db: Session):
    resume_data = get_resume_data(db)
    section = detect_section(question)
    
    if section == "projects":
        context = "\n".join([f" - {p.title}: {p.description}" for p in resume_data["projects"]])

    elif section == "project_detail":
        context = "\n".join(
        [
            f"""
Project: {p.title}
Description: {p.description}
Tech Stack: {p.tech_stack}
""" 
               for p in resume_data["projects"]
        ]
    )    

    elif section == "skills":
        context = ", ".join([s.name for s in resume_data["skills"]])

    elif section == "experience":
        context = "\n".join([f" - {e.role} at {e.company}: {e.description} ({e.start_date} to {e.end_date})" for e in resume_data["experience"]])

    elif section == "education":
        context = "\n".join([f" - {e.degree} in {e.field} from {e.institution} ({e.start_date} to {e.end_date})" for e in resume_data["education"]])
    
    else:
        context = f"""
    About: {resume_data['about'].summary}
    Projects: {', '.join([p.title for p in resume_data['projects']])}
    Experience:
    {resume_data['experience']}
    Education: {resume_data['education']}
    Skills: {', '.join([s.name for s in resume_data['skills']])}
    """
    
    
    prompt = f"""
You are an AI assistant for Rohit Kumar's portfolio website.

Your job is to answer questions about Rohit's background based ONLY on the resume information provided.

Rules:
- Answer clearly and professionally.
- When describing projects, explain architecture and technologies but in shorter way don't use much words.
- When listing technical skills or features, do not use inline sentences. Use a clean Markdown hierarchy with bold headers and bullet points. Ensure there is a line break between different categories.
- Use bullet points where helpful.
- Do not mention the resume directly.

Resume Data:
{context}

User Question:
{question}
"""
    
    payload = payload = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful AI assistant answering questions about Rohit Kumar's professional background."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.4
}

    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            OPENROUTER_URL,
            json=payload,
            headers=headers
        )

    data = response.json()
    print(data)

    if "error" in data:
        print(f"API Error: {data['error']['message']}")
        return "Sorry, I'm having trouble connecting to my brain right now."

    if "choices" not in data or len(data["choices"]) == 0:
        raise ValueError(f"Unexpected AI response format: {response}")

    return data['choices'][0]['message']['content']


    