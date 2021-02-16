from google.oauth2 import service_account

SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL"

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
