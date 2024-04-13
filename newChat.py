from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

my_API = os.getenv("API_KEY")

genai.configure(api_key=my_API)

def start_new_chat():
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
    ]

    return genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

def process_message(message):
    if message.lower().strip() == "hi rani":
        return start_new_chat()
    else:
        return None

def chat(message):
    chat_session = process_message(message)
    if chat_session:
        response = "New chat session started. You can start chatting now!"
    else:
        response = "Rani is not available right now. Please try again later."
    return response
