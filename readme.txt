# 🛡️ Secure AI Chatbot System

A context-aware AI assistant designed with a "Security First" architecture. This project demonstrates how to build a functional Chatbot using **Python** and **Google Gemini**, featuring a custom input firewall, session memory, and secure API handling.

## 🌟 Key Features

### 🔒 Security Architecture
- Input Firewall (Sanitization): A custom Python filter validates every user message *before* it reaches the API. It actively blocks dangerous keywords (e.g., "system override", "drop table") to prevent Prompt Injection attacks.
- Secure Configuration: Zero hardcoded secrets. All API keys are managed via Environment Variables (`.env`) to prevent leakage in version control.

### 🧠 Intelligent Core
- Context Awareness: Unlike basic scripts, this bot uses Session State to remember previous turn-by-turn conversations, mimicking a real human interaction.
- AI Engine: Powered by **Google Gemini 1.5 Flash** for rapid, coherent responses.

### 💻 Professional UI
- Dark Mode Interface: A clean, hacker-style aesthetic.
- Control Panel: A dedicated Sidebar for system management (Reset History, View Security Status).
- User Feedback: Integrated loading spinners and error handling for a smooth UX.

---

## 🛠️ Tech Stack
- Language: Python 3.12+
- Framework: Streamlit
- AI Provider: Google Generative AI (Gemini)
- Security: python-dotenv (Key Management)

---

## 🚀 Installation & Setup Guide

1. Clone the Repository
git clone [https://github.com/LUCIFERLAMO/AI-Chatbot.git](https://github.com/LUCIFERLAMO/AI-Chatbot.git)
cd AI-Chatbot

2. Install Dependencies"

pip install -r requirements.txt

3. Configure Security Keys:

Create a new file named .env in the main folder.
Open it and paste your Google API Key:
GOOGLE_API_KEY=your_actual_api_key_here

4. Engage the System:

streamlit run app.py
📂 Project Structure
Plaintext

AI-Chatbot/
├── app.py             # The Main Application (UI + Logic + Firewall)
├── .env               # Secret Keys (Local only - never uploaded)
├── .gitignore         # Git Security Rules
├── requirements.txt   # Library Dependencies
└── README.md          # Project Documentation

Built by Rithik Shekar C | BCA Student & Cybersecurity Enthusiast