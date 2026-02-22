import httpx
from sqlalchemy.orm import Session
from app.config import settings
from app.services.resume_service import get_resume_data

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

async def generate_ai_response(question: str, db: Session):
    resume_data = get_resume_data(db)

    context = f"""
    About: {resume_data['about'].summary if resume_data['about'] else ''}
    Projects: {', '.join([project.title for project in resume_data['projects']])}
    Experience: {', '.join([experience.role + ' at ' + experience.company for experience in resume_data['experience']])}
    Education: {', '.join([education.institution for education in resume_data['education']]) if resume_data['education'] else ''}
    Skills: {', '.join([skill.name for skill in resume_data['skills']]) }
    """
    
    prompt = f"""
You are an assistant answering questions about Rohit kumar's resume.

Use ONLY the information below.

Resume Information:
{context}

User Question:
{question}
"""
    
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
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


    