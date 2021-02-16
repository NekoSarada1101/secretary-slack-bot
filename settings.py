from google.oauth2 import service_account
SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL"
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
]
SERVICE_ACCOUNT_FILE = 'credentials.json'

CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,
                                                                    scopes=SCOPES)
