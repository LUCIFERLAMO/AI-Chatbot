import os 
from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai

if "history" not in st.session_state:
    st.session_state.history = [] # adding the notebook to it as to not lose the chat history

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")

for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    
if prompt:= st.chat_input("Hello there !!"):

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.history.append({"role":"user","content":prompt})

    with st.spinner("Thinking..."):
        response = model.generate_content(prompt)
        ai_reply = response.text

    with st.chat_message("Ai"):
        st.markdown(ai_reply)

    st.session_state.history.append({"role":"Ai","content":ai_reply})