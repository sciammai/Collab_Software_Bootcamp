import requests
import json
from env import config

token = config['WEBEX_ACCESS_TOKEN']
base_url = config['WEBEX_BASE_URL']

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

endpoint = '/v1/meetings?from=2021-03-09&to=2030-03-09'

Meeting_numb = 0
response = requests.get(url=f"{base_url}{endpoint}", headers=headers).json()
for meeting in response['items']:
    Meeting_numb = Meeting_numb + 1

endpoint2 = '/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vOTk5Y2E5MzAtODBlMS0xMWViLTk0OTEtZjVjNzU0N2EwNmEy'

Messages_numb = 0
response = requests.get(url=f"{base_url}{endpoint2}", headers=headers).json()
for msg in response['items']:
    Messages_numb = Messages_numb + 1

endpoint3 = '/v1/rooms?type=group'

Spaces_numb = 0
response = requests.get(url=f"{base_url}{endpoint3}", headers=headers).json()
for space in response['items']:
    Spaces_numb = Spaces_numb + 1

print(Meeting_numb)
print(Messages_numb)
print(Spaces_numb)

endpoint4 = '/v1/messages'

body ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vOTk5Y2E5MzAtODBlMS0xMWViLTk0OTEtZjVjNzU0N2EwNmEy",
    "text": f"Information sharing: Total number of scheduled Meetings: {Meeting_numb}. Total number of Spaces I am part of: {Spaces_numb}. Total number of Messages I sent in this space until now: {Messages_numb}."
}

response = requests.post(url=f"{base_url}{endpoint4}", headers=headers, data=json.dumps(body)).json()
