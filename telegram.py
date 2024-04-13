# Basic Telegram Bot using pytelegrambotapi
from dotenv import load_dotenv
# 
import telebot
import os
# from chatbot import func
from chatbot import UserSession
load_dotenv()

user_sessions = {}



# Create the bot object to interact with the Telegram API
bot = telebot.TeleBot(os.getenv("TG_KEY"))


def get_or_create_session(user_id, name):
    if user_id not in user_sessions:
        user_sessions[user_id] = UserSession(user_id, name)
    return user_sessions[user_id]




@bot.message_handler(func=lambda message: message.chat.type == 'group')
def handle_message(message):
    print(message)
    user_id = message.chat.id
    name  = message.from_user.first_name
    user_session = get_or_create_session(user_id, name)
    response = user_session.func(message.text + f'(from {message.from_user.first_name})  NOTE :DO NOT ADD (from <your name>)(IMPORTANT) AT THE END OF YOUR MESSAGE.')
    bot.send_message(user_id, response)


bot.infinity_polling()
