import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n***Get Current Weather condition***\n")

    city = input("\nPlease Enter the city:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    print(f"\nCurrent Weather for {weather_data["name"]}")
    print(f"\nThe Temp is {weather_data["main"]["temp"]}")
    print(f"\nFeels Like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"].capitalize()}.")

if __name__ == "__main__":
    get_current_weather()