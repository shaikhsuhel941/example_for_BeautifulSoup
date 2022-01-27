from anyio import CapacityLimiter
import requests
from pprint import pprint

API_key = '0c39b8a10c0d286ce9ce52c6004439e8'
city = input('Enter city name : ')

url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}"

weather_data = requests.get(url).json()

pprint(weather_data)