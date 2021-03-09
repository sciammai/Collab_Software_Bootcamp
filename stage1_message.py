import requests
import json
from env import config

token = config['WEBEX_ACCESS_TOKEN']
base_url = config['WEBEX_BASE_URL']
endpoint = '/v1/messages'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

message ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vOTk5Y2E5MzAtODBlMS0xMWViLTk0OTEtZjVjNzU0N2EwNmEy",
    "text":"Welcome everybody!"
}

response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(message)).json()