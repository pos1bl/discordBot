import discord
from discord.ext import commands

description = '''An example bot to respond with "OK BOSS" to every user message.'''

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_message(message):
    if message.author.bot:  # Ігноруємо повідомлення від інших ботів
        return
    
    await message.channel.send("OK BOSS")  # Відповідаємо на кожне повідомлення словом "OK BOSS"


bot.run(token)

