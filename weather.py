import json
import requests
from datetime import datetime
from settings import *


def post_weather():
    weather_data = fetch_current_weather_data()  # type: dict
    payload = create_weather_payload(weather_data)  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)


def fetch_current_weather_data() -> dict:
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&"
           "exclude=daily,minutely,hourly,alerts&units=metric&lang=ja"
           .format(LAT_LNG[0], LAT_LNG[1], OPEN_WEATHER_API_KEY))  # type: str
    response = requests.get(url)
    print(response)
    weather_data = json.loads(response.text)  # type: dict
    return weather_data


def create_weather_payload(weather_data: dict) -> json:
    date = datetime.fromtimestamp(weather_data["current"]["dt"]).strftime(
        "%m/%d %H:%M")  # type: str
    weather = weather_data["current"]["weather"][0]["description"]  # type: str
    image = weather_data["current"]["weather"][0]["icon"]  # type: str
    temp = str(round(weather_data["current"]["temp"], 1)) + "°C"  # type: str
    wind_speed = str(weather_data["current"]["wind_speed"]) + "m/h"  # type: str
    humidity = str(weather_data["current"]["humidity"]) + "%"  # type: str

    data = {  # type: dict
        "response_type": "ephemeral",
        "text": date + "の天気をお知らせします。",
        "attachments": [
            {
                "text": "*" + date + "の天気* ： `" + weather + "`",
                "color": "33ff66",
                "image_url": "http://openweathermap.org/img/wn/" + image + "@2x.png"
            },
            {
                "color": "00BFFF",
                "text": " *気温* ： `" + temp + "`"
            },
            {
                "color": "FFFFFF",
                "text": " *風速* ： `" + wind_speed + "`"
            },
            {
                "color": "5579EC",
                "text": " *湿度* ： `" + humidity + "`"
            },

        ]
    }

    print(data)
    json_data = json.dumps(data).encode("utf-8")  # type: json
    return json_data


if __name__ == "__main__":
    post_weather()
