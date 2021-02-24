from flask import Flask, request
import requests
import json
import google_calendar
import current_weather
import rain_notice
import talking
import wikipedia
from settings import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    data = {
        "text": "hello_world"
    }

    # Slackでは両方とも表示された
    json_data = json.dumps(data).encode("utf-8")
    response = requests.post(
        SLACK_WEBHOOK_URL,
        json_data)
    print(response)
    return 'Hello World!'


@app.route('/calendar', methods=['POST'])
def calendar():
    google_calendar.post_calendar()
    # TODO: FlaskのTypeErrorが発生するのを修正する


@app.route('/weather', methods=['POST'])
def weather():
    current_weather.post_weather()
    # TODO: FlaskのTypeErrorが発生するのを修正する


@app.route('/rain', methods=['POST'])
def rain():
    rain_notice.post_rain_notice()


@app.route('/talk', methods=['POST'])
def talk():
    text = request.form.get('text')  # type: str
    talking.post_talk(text)


@app.route('/wiki', methods=['POST'])
def wiki():
    text = request.form.get('text')  # type: str
    wikipedia.post_wiki(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
