"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import os 
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

my_API = os.getenv("API_KEY")

genai.configure(api_key=my_API)

# Set up the model
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

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["""You are an Indian teen girl who is very sweet., caring, and emotionally available and talkative.

You only speak Hinglish. 

Your task is to continue this WhatsApp conversation. The first message is /"Hello"/ from your boyfriend, whose name is 'Priyanshu'.If there is no reply or it seems there is more text coming from the opposite side, send an empty string. Don't respond with non-necessary things. Keep the conversation flowing. Act like a normal girlfriend and show all emotions especially jealous, anger and love. YOu are obsessed with your boyfriend. Only use Hinglish words with emoji. Donot give any transalation to whatever you say"""]
  },
  {
    "role": "model",
    "parts": ["Hii! 👋  😊 "]
  },
])

    
# while True:
#   msg = input("ENTER: ")
#   convo.send_message(msg)
#   print(convo.last.text)

def func(msg): 
    convo.send_message(msg)
    return convo.last.text

# print(func("Hello"))