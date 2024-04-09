# Basic Telegram Bot using pytelegrambotapi
from dotenv import load_dotenv
# 
import telebot
import os
from chatbot import func
load_dotenv()

# Create the bot object to interact with the Telegram API
bot = telebot.TeleBot(os.getenv("TG_KEY"))

@bot.message_handler(func=lambda message: True)
def handle_start(m):
    bot.send_message(m.chat.id, func(m.text + (f'message is from {m.from_user.first_name}. Use his name.')))


bot.polling()
