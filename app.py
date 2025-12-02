import os 
from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai

# -------The UI Configuration --------
st.set_page_config(
    page_title="Secure_Chat",
    layout="centered",
)

# Loading the API_key
load_dotenv()

# ----- Setup and Security -----

sys_prompt = """
You are a Senior Cybersecurity Expert named Robert.
1. Answer all questions with a focus on safety and best practices.
2. If the user asks about illegal hacking, warn them about the legal consequences.
3. Keep your answers concise and professional.
"""

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_model():
    return genai.GenerativeModel("gemini-2.5-pro", system_instruction=sys_prompt)

model = get_model()

# ----- Sidebar -----

with st.sidebar:
    st.title("Control Panel")
    st.markdown("---")
    st.write("Security Level : HIGH")
    st.write("Model : Gemini 2.5 Pro")

    # ----- The nuke button -----

    if st.button("Clear chat history "):
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()

    st.markdown("---")
    st.caption("Built by RITHIK SHEKAR C ")
    st.caption("2025 secure AI System")

# ----- Main Chat Logic -----

 #Initializing the chat session

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("Secure AI Chat System")

 # Display chat messages from history on app rerun

for message in st.session_state.chat.history:
    role = "User" if message.role == "user" else "Assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

 # Accepting user input

if prompt := st.chat_input("What's Going on in your mind ?"):
    # Display user message in chat message container
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Loading..."):

            # Get the response from the model
            try:
                result = st.session_state.chat.send_message(prompt)
                respond = result.text
                st.markdown(respond)

            except Exception as e:
                print(f"Error as {e}")

