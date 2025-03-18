import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
