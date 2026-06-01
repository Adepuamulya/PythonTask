import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("project_knowledge.txt", "r", encoding="utf-8") as f:
    PROJECT_DATA = f.read()

def get_response(question):

    prompt = f"""
    You are an AI assistant for a Library Management System Project.

    Project Information:
    {PROJECT_DATA}

    Answer only using the project information above.

    User Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text