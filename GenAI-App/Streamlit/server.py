from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class ChatRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask(request: ChatRequest):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.question
        )

        return {
            "response": response.text
        }

    except Exception as e:

        return {
            "response": f"Error: {str(e)}"
        }