import streamlit as st
from llm_client import ask_model

st.set_page_config(page_title="Local LLM Chat", layout="wide")
st.title("Chat with Local LLM")

# Container to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Input box for user message
# chat_input allows "Enter" key to submit automatically
user_input = st.chat_input("Ask me anything...")  # hint appears when empty

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message immediately
    st.chat_message("user").write(user_input)
    
    # Get model reply
    reply = ask_model(user_input)
    
    # Append and display model reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
