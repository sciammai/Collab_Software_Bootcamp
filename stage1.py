import requests
import json
import fileinput
from env import config

token = config['WEBEX_ACCESS_TOKEN']
base_url = config['WEBEX_BASE_URL']
endpoint = '/v1/rooms'

headers = {
    'Authorization' : f'Bearer {token}',
    'Content-Type' : 'application/json'
}

test_room ={
    "title" : "Test Room"
}

response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(test_room)).json()
     
roomid=response['id']
print(roomid)

# Read in the file
with open('env.py', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('<Replace me in stage 1>', roomid)

# Write the file out again
with open('env.py', 'w') as file:
    file.write(filedata)


