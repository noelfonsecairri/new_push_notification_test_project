import uuid, requests, json, datetime, pprint

from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import OAuth2Credentials
from apiclient import discovery

def main_function():
  ep = (
          lambda yr, mo, dd, hh, mm: int(
              datetime.datetime(yr, mo, dd, hh, mm).timestamp()
          )
          * 1000
      )
  API = "drive"
  API_VERSION = "v3"
  SCOPES = ['https://www.googleapis.com/auth/drive.file',
           'https://www.googleapis.com/auth/drive.readonly',
           'https://www.googleapis.com/auth/drive']

  credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'drive_push_notifications_3.json', scopes=SCOPES)

  drive_service = discovery.build(API, API_VERSION, credentials=credentials)
  access_token_info = credentials.get_access_token()
  # print(access_token_info.access_token) #check to see the value of the token

  # this is a randomly generated id to be passed to the payload
  channel_id = str(uuid.uuid4())
  token = access_token_info.access_token
  url_webhook = "https://api.noelfonseca.com/notifications"
  gfolder_id = "1IMniHYS6wBUG31MWd_4nTIkBgpc-Llrz"
  header = {
      'Auth': f'Bearer {token}',
      'Content-Type': 'application/json'
  }
  body = {
      "id": channel_id,
      "expiration": ep(2020, 12, 20, 8, 53),
      "type": "web_hook",
      "address": f'{url_webhook}',
      "token": token
  }

  file_id = f'{gfolder_id}'


# use files().watch(), not changes().watch to monitor changes to folders. source: https://stackoverflow.com/questions/18144094/google-drive-sdk-push-notifications-watch-changes-on-all-files/18151189#18151189
  response = drive_service.files().watch(fileId=gfolder_id, body=body).execute()

  response2 = drive_service.files().list().execute()



  pprint.pprint(response)
  pprint.pprint(response2)

  if response:
    print('hello world!')

if __name__ == "__main__":
  main_function()