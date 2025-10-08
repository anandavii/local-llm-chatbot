import streamlit as st
from llm_client import ask_model

st.title("Local LLM Chatbot")

# Session state to keep conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Call your local LLM
    response = ask_model(user_input)
    
    # Append messages to session
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")
