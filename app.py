import discord
from discord.ext import commands
from discord.ext import slash_commands
import os
from dotenv import load_dotenv
from weather import get_weather
# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True  # Critical for reading messages
intents.guilds = True
intents.members = True

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online and ready to rock!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your Lofi Radio Bot 🎶")

@bot.command()
async def weather(ctx, *, city: str = None):
    """Get weather info for a city."""
    if city is None or city == "": 
        await ctx.send("You forgot to provide a city! 🌆")
        return
    weather, temperature = get_weather(city)
    
    if weather:
        await ctx.send(f"It's {temperature}°C in {city} and the weather is {weather}. ☁️")
    else:
        await ctx.send(f"I can't find your city, is this **{city}** place even exists> 🤔")

bot.run(TOKEN)
