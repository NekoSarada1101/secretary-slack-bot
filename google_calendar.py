import json
import requests
import googleapiclient.discovery
from datetime import datetime, timedelta, timezone
from settings import CREDENTIALS, SLACK_WEBHOOK_URL, CALENDAR_ID_LIST

service = googleapiclient.discovery.build(
    'calendar', 'v3', credentials=CREDENTIALS)


def post_calendar(date):
    if date is not None:
        select_date = datetime.strptime(date + '+0900', '%Y-%m-%d%z')
    else:
        select_date = datetime.now(timezone(timedelta(hours=+9), 'JST'))

    calendar_event_list = fetch_all_calendar_event_list(select_date)  # type: list
    payload = create_calendar_payload(
        calendar_event_list,
        select_date)  # type: json
    response = requests.post(SLACK_WEBHOOK_URL, payload)
    return response


def fetch_all_calendar_event_list(select_date) -> list:
    calendar_event_list = []  # type: list
    for calendar_id in CALENDAR_ID_LIST:
        calendar_event_list.append(
            fetch_calendar_event_list(calendar_id, select_date))

    return calendar_event_list


def fetch_calendar_event_list(calendar_id: str, select_date: datetime) -> str:
    time_min = select_date.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%dT%H:%M:%S%z")  # type: str
    time_max = select_date.replace(hour=23, minute=59, second=59).strftime("%Y-%m-%dT%H:%M:%S%z")  # type: str
    print({'calendar_id': calendar_id, 'time_min': time_min, 'time_max': time_max})

    page_token = None
    while True:
        events = service.events().list(
            calendarId=calendar_id,
            pageToken=page_token,
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime").execute()  # type: dict
        list_text = ""  # type: str
        for event in events['items']:
            start = event['start'].get(
                'dateTime', event['start'].get('date'))  # type: str

            word_count = 10  # type: int
            if len(start) == word_count:
                start = datetime.strptime(start, "%Y-%m-%d").strftime("%m/%d ")
                list_text += start
            else:
                start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").strftime("%m/%d  %H:%M-")
                end = event['end'].get('dateTime', event['end'].get('date'))  # type: str
                end = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S%z").strftime("%H:%M ")
                list_text += start + end

            list_text += "`" + event['summary'] + "`" + "\n"

        page_token = events.get('nextPageToken')
        if page_token is None:
            break

    return list_text


def create_calendar_payload(
        calendar_data: list,
        select_date: datetime) -> json:
    summary_list = []  # type: list
    for calendar_id in CALENDAR_ID_LIST:
        calendar = service.calendars().get(calendarId=calendar_id).execute()  # type: dict
        summary_list.append(calendar["summary"])

    attachments = []  # type: list
    color_list = ["FF0000", "00BFFF", "FFFF00", "FFFFFF"]
    for i in range(len(calendar_data)):
        attachments.append(
            {
                "color": color_list[i],
                "title": summary_list[i],
                "text": calendar_data[i]
            }
        )

    data = {  # type: dict
        "response_type": "ephemeral",
        "text": select_date.strftime("%m月%d日") + "の予定をお知らせします。",
        "attachments":
            attachments
    }
    print(data)
    json_data = json.dumps(data).encode("utf-8")  # type: json
    return json_data


if __name__ == "__main__":
    post_calendar()
