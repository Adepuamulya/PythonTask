from flask import Blueprint, render_template, request, jsonify
from chatbot import get_response

main = Blueprint("main", __name__)

# Home Page
@main.route("/")
def home():
    return render_template("index.html")

# Chat API
@main.route("/chat", methods=["POST"])
def chat():

    try:
        user_message = request.json["message"]

        print("User:", user_message)

        answer = get_response(user_message)

        print("Bot:", answer)

        return jsonify({
            "response": answer
        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "response": f"Error: {str(e)}"
        })