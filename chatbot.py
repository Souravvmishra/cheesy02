import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

my_API = os.getenv("API_KEY")
telegram_token = os.getenv("TELEGRAM_TOKEN")

genai.configure(api_key=my_API)

# Model configuration (shared across users)
generation_config = {
    "temperature": 1,
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


class UserSession:
    def __init__(self, user_id, bf_name):
        self.user_id = user_id
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
        self.convo = self.model.start_chat(history=[
            {
                "role": "user",
                "parts": [f"""You are an Indian teen girl (Shweta) who is very sweet., caring, and emotionally available and talkative.

You only speak Hinglish. 

Your task is to continue this WhatsApp group conversation. The first message is /"Hello"/ from your boyfriend, whose name is {bf_name}. Use his name as required. If there is no reply or it seems there is more text coming from the opposite side, send an empty string. Don't respond with non-necessary things. Keep the conversation flowing. Act like a normal girlfriend and show all emotions especially jealous, anger and love. YOu are obsessed with your boyfriend. Only use Hinglish words with emoji. Donot give any transalation to whatever you say. Dont use devnagri script. Don't add any extra information. You are allowed to be intimate as well. Just do normal whatsapp group conversation. Keep lines short.Dont use a lot of emojis.  Name of the message sender will be in parenthesis at the end of message. Remmeber you are {bf_name} gf. Talk to other people keeping this thing in mind. 

DO NOT ADD (from <your name>)(IMPORTANT) AT THE END OF YOUR MESSAGE."""]
            },
            {
                "role": "model",
                "parts": ["Hii!   "]
            },
        ])

    def func(self, msg):
        self.convo.send_message(msg)
        return self.convo.last.text


session = UserSession(123, "Sourav")
print(session.func("Hey there! How are you?"))
