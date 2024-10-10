import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def getWeather():
    print("\n***Get Current Weather condition***\n")

    city = input("Please Enter the City Name:\n")

    request_URL = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric"

    # print(request_URL)

    weather_data = requests.get(request_URL).json()
    # pprint (weather_data)
    print (f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')

getWeather()