from flask import Flask, request
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


@app.route('/', methods=['POST'])
def hello_world():
    post_data = request.get_data()  # type: str
    print(post_data)

    text = request.form.get('text')
    text_list = text.split()
    print(text_list)

    if text_list[0] == "calendar":
        google_calendar.post_calendar()
    elif text_list[0] == "weather":
        current_weather.post_weather()
    elif text_list[0] == "wiki":
        wikipedia.post_wiki(word=text[1])
    elif text_list[0] == "url":
        bitly.post_bitly_url(long_url=text[1])
    else:
        talking.post_talk(word=text[0])


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
