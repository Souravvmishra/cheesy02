import discord
import os 
from dotenv import load_dotenv
from chatbot import func

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        msg = func(message.content)
        await message.reply(msg, mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

token = os.getenv("DISCORD")
client.run(token)