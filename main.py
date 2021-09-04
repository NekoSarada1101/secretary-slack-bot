from flask import Flask, request, make_response
import requests
import json
import google_calendar
import current_weather
import rain_notice
import talking
import wikipedia
import bitly
from settings import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/slackbot', methods=['POST'])
def slack_bot():
    post_data = request.get_data()  # type: str
    print(post_data)

    text = request.form.get('text')
    text_list = text.split(' ')
    print(text_list)

    if text_list[0] == "calendar":
        text = text_list[1] if len(text_list) == 2 else None
        google_calendar.post_calendar(text)
    elif text_list[0] == "weather":
        current_weather.post_weather(text_list[1])
    elif text_list[0] == "wiki":
        wikipedia.post_wiki(text_list[1])
    elif text_list[0] == "url":
        bitly.post_bitly_url(text_list[1])
    elif text_list[0] == 'talk':
        talking.post_talk(text_list[1])
    return make_response('', 200)


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


@app.route('/url', methods=['POST'])
def url():
    long_url = request.form.get('text')  # type: str
    bitly.post_bitly_url(long_url)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
