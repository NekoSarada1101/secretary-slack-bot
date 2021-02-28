import requests
import json
import urllib.parse
from settings import *


def post_wiki(word: str):
    parse = urllib.parse.quote(word)  # type: str
    url = "http://ja.wikipedia.org/wiki/" + parse  # type: str
    print(url)

    data = {  # type: dict
        "text": url,
        "unfurl_links": "true"
    }
    print(data)
    json_data = json.dumps(data).encode("utf-8")  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, json_data)
    print(response)


if __name__ == "__main__":
    post_wiki("スペクトル")
