import requests
from config import WEATHER_API_KEY, WEATHER_BASE_URL

def get_weather(city):
    """Fetches weather data from OpenWeatherMap."""
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(WEATHER_BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        return weather, temperature
    else:
        return None, None
