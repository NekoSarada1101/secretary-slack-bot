import json
import requests
from settings import *


def post_rain_notice():
    weather_data = fetch_hourly_weather_data()  # type: dict
    payload = create_rain_notice_payload(weather_data)  # type: json
    if payload is not None:
        response = requests.post(SLACK_WEBHOOK_URL, payload)
        print(response)


def fetch_hourly_weather_data() -> dict:
    url = ("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&"
           "exclude=current,daily,minutely,alerts&units=metric&lang=ja"
           .format(LAT_LNG[0], LAT_LNG[1], OPEN_WEATHER_API_KEY))  # type: str
    response = requests.get(url)
    print(response)
    weather_data = json.loads(response.text)  # type: dict
    return weather_data


def create_rain_notice_payload(weather_data: dict) -> json:
    try:
        precipitation = weather_data["hourly"][0]["rain"]["1h"]
    except KeyError:
        print("No rain.")
        return

    precipitation_level = [10, 20, 30, 50, 80]
    if precipitation < precipitation_level[0]:
        message = "弱い雨が降りそうです。\n傘があると良いかもしれません。\n"
    elif precipitation < precipitation_level[1]:
        message = "やや強い雨が降りそうです。\n傘があると良いかもしれません。\n"
    elif precipitation < precipitation_level[2]:
        message = "強い雨が降りそうです。\n傘があると良いかもしれません。\n"
    elif precipitation < precipitation_level[3]:
        message = "激しい雨が降りそうです。\n外出は控えたほうが良いかもしれません。\n"
    elif precipitation < precipitation_level[4]:
        message = "非常に激しい雨が降りそうです。\n危険ですので外出はやめましょう。\n"
    else:
        message = "猛烈な雨が降りそうです。\n危険ですので外出はやめましょう。\n"

    data = {"text": "<@{}>{}【1時間以内の予想降水量：{}mm/h】".format(SLACK_USER_ID, message, precipitation)}

    print(data)
    json_data = json.dumps(data).encode("utf-8")  # type: json
    return json_data


if __name__ == "__main__":
    post_rain_notice()
