import json
import requests
from settings import *


def post_talk(word: str):
    message = fetch_talk_message(word)
    payload = create_talk_payload(message)
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)


def fetch_talk_message(word: str) -> str:
    payload = {
        "apikey": A3RT_API_KEY,
        "query": word
    }

    response = requests.post("https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk", payload)
    print(response.text)
    data = json.loads(response.text)
    message = data["results"][0]["reply"]
    print(message)

    return message


def create_talk_payload(message: str) -> json:
    data = {  # type: dict
        "text": message,
    }

    print(data)
    json_data = json.dumps(data).encode("utf-8")  # type: json
    return json_data


if __name__ == "__main__":
    text = "おはよう"
    post_talk(text)
