from google.oauth2 import service_account

SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL"

SLACK_USER_ID = "SLACK_USER_ID"

CALENDAR_ID_LIST = [
    "CALENDAR_ID_1",
    "CALENDAR_ID_2",
    "CALENDAR_ID_3",
]

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
]
SERVICE_ACCOUNT_FILE = 'credentials.json'

CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,
                                                                    scopes=SCOPES)

OPEN_WEATHER_API_KEY = "OPEN_WEATHER_API_KEY"
LAT_LNG = ["LAT", "LNG"]
