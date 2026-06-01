from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def generate_openai_response(prompt: str) -> str:
    try:
        response = openai_client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            max_output_tokens=300,
            temperature=0.7,
        )

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
    except Exception as exc:
        return f"Error generating response: {exc}"


@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    ai_response = ""

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            if not OPENAI_API_KEY:
                ai_response = "OpenAI API key not configured. Set OPENAI_API_KEY in .env."
            else:
                ai_response = generate_openai_response(prompt)

    return render_template("index.html", prompt=prompt, response=ai_response)


if __name__ == "__main__":
    app.run(debug=True)