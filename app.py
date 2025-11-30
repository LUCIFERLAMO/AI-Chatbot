import os 
from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Genai Chat-Bot")
st.caption("Made by Rithik shekar c using google gemini 2.5 flash model")

prompt =st.text_input("Whats going on your mind , Happy to help you!")

st.write ("**User Prompt** : " + prompt)
if prompt:
    with st.spinner("Generating response..."):
        response = model.generate_content(prompt)

    st.write(f"*AI Response* :  {response.text}*")