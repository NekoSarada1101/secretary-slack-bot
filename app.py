from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    data = {
        "text": "hello_world"
    }

    # Slackでは両方とも表示された
    json_data = json.dumps(data).encode("utf-8")
    response = requests.post(
        "https://hooks.slack.com/services/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",
        json_data)
    print(response)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
