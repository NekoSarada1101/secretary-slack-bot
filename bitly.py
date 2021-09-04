import requests
import json
from settings import SLACK_WEBHOOK_URL, BITLY_API_ACCESS_TOKEN


def post_bitly_url(long_url: str):
    bitly_data = fetch_shorten_url(long_url)  # type: dict
    payload = create_bitly_payload(bitly_data)  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    print(response)


def fetch_shorten_url(long_url: str) -> dict:
    endpoint_url = "https://api-ssl.bitly.com/v3/shorten?access_token={}&longUrl={}".format(BITLY_API_ACCESS_TOKEN, long_url)  # type: str

    response = requests.post(endpoint_url)
    print(response.text)

    bitly_data = json.loads(response.text)  # type: dict
    return bitly_data


def create_bitly_payload(bitly_data: dict) -> json:
    data = {
        "text": "URLを短くしました！\n" + bitly_data["data"]["url"]
    }
    print(data)
    json_data = json.dumps(data).encode("utf-8")
    return json_data


if __name__ == "__main__":
    post_bitly_url(
        "https://www.amazon.co.jp/gp/product/B08CRCZ4NX?pf_rd_r=JDM5NDW5NKR5MMFV84PW&pf_rd_p=7626af39-b716-47c8-84eb-9679f177dc53&pd_rd_r=bcb48d8a-cda9-4271-a31f-27d2ad01ee14&pd_rd_w=BHl2Y&pd_rd_wg=3SXZe&ref_=pd_gw_unk")
