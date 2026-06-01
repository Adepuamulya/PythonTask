import streamlit as st
import requests

st.set_page_config(
    page_title="Gemini ChatBot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Gemini ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask me anything...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={
                    "question": question
                }
            )

            answer = response.json()["response"]

            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })