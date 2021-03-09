import requests
import json
import fileinput
from env import config

token = config['WEBEX_ACCESS_TOKEN']
base_url = config['WEBEX_BASE_URL']
endpoint = '/v1/rooms?type=group'

headers = {
    'Authorization' : f'Bearer {token}',
    'Content-Type' : 'application/json'
}

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        get_rooms = response.json()
        rooms = get_rooms['items']
        for room in rooms:
            if room['title'] == "CSAP Programmability CTF - Team 2":
                roomid=room['id']
                print(roomid)

    # Read in the file
    with open('env.py', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('<Replace me in stage 0>', roomid)

    # Write the file out again
    with open('env.py', 'w') as file:
        file.write(filedata)

except Exception as ex:
    print(ex)