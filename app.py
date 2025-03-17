import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    
    if message.author == bot.user:
        return
    
    if message.content == 'ping':
        await message.channel.send('pong')
    elif message.content == 'pong':
        await message.channel.send('ping')
    
    if message.content == 'hello':
        await message.channel.send('world')

bot.run(os.getenv('TOKEN'))
