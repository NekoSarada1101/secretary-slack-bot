import json
import requests
from settings import *


def post_weather():
    weather_data = fetch_current_weather_data()  # type: dict


def fetch_current_weather_data() -> dict:
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&"
           "exclude=daily,minutely,hourly,alerts&units=metric&lang=ja"
           .format(LAT_LNG[0], LAT_LNG[1], OPEN_WEATHER_API_KEY))  # type: str
    response = requests.get(url)
    print(response)
    weather_data = json.loads(response.text)  # type: dict
    return weather_data
