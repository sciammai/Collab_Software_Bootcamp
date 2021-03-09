import requests
import json
from env import config

token = config['WEBEX_ACCESS_TOKEN']
base_url = config['WEBEX_BASE_URL']
endpoint = '/v1/memberships'

headers = {
    'Authorization' : f'Bearer {token}',
    'Content-Type' : 'application/json'
}

person1 ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vOTk5Y2E5MzAtODBlMS0xMWViLTk0OTEtZjVjNzU0N2EwNmEy",
    "personEmail":"mneiding@cisco.com"
}

person2 ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vOTk5Y2E5MzAtODBlMS0xMWViLTk0OTEtZjVjNzU0N2EwNmEy",
    "personEmail":"frewagne@cisco.com"
}


response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(person1)).json()
response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(person2)).json()