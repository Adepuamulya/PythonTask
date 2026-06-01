from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-2.5-flash"

# System Prompt
SYSTEM_PROMPT = """
You are a Python Learning Assistant.

Rules:
- Answer only Python, FastAPI, Flask, AI/ML, and software development questions.
- Be beginner friendly.
- Give examples when needed.
- Keep answers clear and structured.
"""

class ChatRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask(request: ChatRequest):

    question = request.question

    prompt = f"""
    {SYSTEM_PROMPT}

    User Question:
    {question}
    """

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return {
            "response": response.text
        }

    except Exception as e:
        return {
            "response": f"Error: {str(e)}"
        }