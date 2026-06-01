from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
openai_client = OpenAI(api_key=OPENAI_API_KEY)


class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gpt-4o-mini"


def extract_text(response) -> str:
    if hasattr(response, "output_text") and response.output_text:
        return response.output_text.strip()

    if getattr(response, "output", None):
        output = response.output
        if isinstance(output, list) and len(output) > 0:
            first = output[0]
            if isinstance(first, dict) and "content" in first:
                content = first["content"]
                if isinstance(content, list) and len(content) > 0:
                    text_value = content[0].get("text") if isinstance(content[0], dict) else None
                    if text_value:
                        return text_value.strip()

    return ""


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "GenAI FastAPI running"}


@app.post("/generate")
async def generate(prompt_request: PromptRequest):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured.")

    try:
        response = openai_client.responses.create(
            model=prompt_request.model,
            input=prompt_request.prompt,
            max_output_tokens=300,
            temperature=0.7,
        )
        answer = extract_text(response)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    return {
        "prompt": prompt_request.prompt,
        "model": prompt_request.model,
        "response": answer,
    }