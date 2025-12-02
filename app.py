import os 
from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("MY Gemini-2.5-Flash Chatbot")
st.caption("Made by Rithik shekar c")

#creating the memory 

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[]) # It wont forget previous messages "history=[]" gemnin object 

# Display the chat messages 

for message in st.session_state.chat.history:   # Google uses 'role': 'user' or 'model'. Streamlit needs 'user' or 'assistant'.
    role ="user" if message.role == "user" else "Assissant" 
    with st.chat_message(role):
        st.markdown(message.parts[0].text) # Display the text part of the message 

# Message(
#     role="user",
#     parts=[
#         Part(text="Hello there")  # message.parts[0]
#         Part(text="How are you?") # message.parts[1]
#     ]
# )
# """" comment """" streamlit cant display multiple parts 
 
    
if prompt:= st.chat_input("Whats there on your mind?"):

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("Assissant"):
        with st.spinner("Thinking...."):
            try:
                response = st.session_state.chat.send_message(prompt)
                ai_response =response.text
                st.markdown(ai_response)
                
            except Exception as e:
                st.error(f"Error: {e}")

    