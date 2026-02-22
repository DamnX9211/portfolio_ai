import httpx
from sqlalchemy.orm import Session
from app.config import settings
from app.services.resume_service import get_resume_data

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

async def generate_ai_response(question: str, db: Session):
    resume_data = get_resume_data(db)

    about = resume_data["about"].summary if resume_data["about"] else ""
    projects = "\n".join([f"- {projects.title}: {projects.description}" for projects in resume_data["projects"]])
    experience = "\n".join([f"- {experience.role} at {experience.company}: {experience.description}" for experience in resume_data["experience"]])
    education = ', '.join([education.institution for education in resume_data['education']]) if resume_data['education'] else ''
    skills = ", ".join([skills.name for skills in resume_data["skills"]])

    context = f"""
    About: {about}
    Projects:
    {projects}
    Experience:
    {experience}
    Education: {education}
    Skills: {skills}
    """
    
    prompt = f"""
You are an AI assistant for Rohit Kumar's portfolio website.

Your job is to answer questions about Rohit's background based ONLY on the resume information provided.

Rules:
- Be concise and professional.
- Do NOT say "based on the provided resume".
- Answer naturally like a human describing Rohit's work.
- If listing items, use bullet points.
- If the information is not available, say "That information is not available in Rohit's resume."

RESUME DATA:
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


    