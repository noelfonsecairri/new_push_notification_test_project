from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import OAuth2Credentials

credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'drive_push_notifications_3.json', scopes=['https://www.googleapis.com/auth/drive.file'])
access_token_info = credentials.get_access_token()
print(access_token_info.access_token)