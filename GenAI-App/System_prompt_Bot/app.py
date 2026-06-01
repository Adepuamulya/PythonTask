import streamlit as st
import requests

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="System Prompt Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("🚀 System Prompt Bot")

# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# Display Previous Messages
# ==========================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ==========================================
# Chat Input
# ==========================================

question = st.chat_input("Ask a question")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    # Get response from FastAPI
    with st.spinner("Thinking..."):

        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )

            answer = response.json().get(
                "response",
                "No response received."
            )

        except Exception as e:
            answer = f"Error: {str(e)}"

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)