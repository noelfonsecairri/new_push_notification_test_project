import uuid
import requests
import json

from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import OAuth2Credentials


SCOPES = ['https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive.readonly',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'drive_push_notifications_3.json', scopes=SCOPES)

access_token_info = credentials.get_access_token()

print(access_token_info.access_token)

# this is a randomly generated id to be passed to the payload
channel_id = str(uuid.uuid4())
# setting up scope for 

# get secret token from step 3

token = access_token_info.access_token
url_webhook = "https://api.noelfonseca.com/notifications"
gfolder_id = "14gG8_SQwn7zPaRX_AvtyVSe91NbrUQZc"

header = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body = {
    "id": channel_id,
    "type": "web_hook",
    "address": f'{url_webhook}'
}

file_id = f'{gfolder_id}'


r = requests.post(url=f'https://www.googleapis.com/drive/v3/file/{file_id}/watch?pageToken=766', 
                  data=json.dumps(body), headers=header)

print(r)