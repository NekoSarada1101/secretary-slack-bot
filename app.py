from flask import Flask
import requests
import json
import google_calendar
import weather
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
def calendar():
    weather.post_weather()
    # TODO: FlaskのTypeErrorが発生するのを修正する


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
