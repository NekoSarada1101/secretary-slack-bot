import json
import requests
from settings import *


def post_rain_notice():
    weather_data = fetch_hourly_weather_data()  # type: dict


def fetch_hourly_weather_data() -> dict:
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&"
           "exclude=current,daily,minutely,alerts&units=metric&lang=ja"
           .format(LAT_LNG[0], LAT_LNG[1], OPEN_WEATHER_API_KEY))  # type: str
    response = requests.get(url)
    print(response)
    weather_data = json.loads(response.text)  # type: dict
    return weather_data


if __name__ == "__main__":
    post_rain_notice()
