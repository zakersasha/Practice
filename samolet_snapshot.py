import os

import requests

import json


def get_camera_snapshot():
    # Get first access and refresh tokens
    # access_token, refresh_token = refresh_tokens(os.environ.get('REFRESH_TOKEN'))
    # if refresh_token == 0:
    #     return access_token, refresh_token
    # data = {
    #     'start_time': 1654239000,
    #     'end_time': 1654239600
    # }
    # data = json.dumps(data)
    access_token = 'xtok-100U95-415d184feb7b4bbf8d683ab2198a4a11-gdZXMnUYVOvJW0dx'
    # Call camera api
    camera_response = requests.get(
        f'https://openapi-alpha-eu01.ivideon.com/cameras/100-vmmZtRWyfBO920tMHRUas6:0/live_preview?access_token={access_token}', timeout=20)

    snapshot = camera_response.content
    print(snapshot)

    if type(snapshot) == bytes:
        status = 1
    else:
        status = 0
    return snapshot, status


def refresh_tokens(refresh_token):
    # Refresh access token and get new refresh
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'refresh_token={refresh_token}&grant_type=refresh_token'

    # Call token api
    response = requests.post('https://api.ivideon.com/auth/oauth/token', headers=headers, data=data,
                             auth=(os.environ.get('CLIENT_ID'), os.environ.get('CLIENT_SECRET')))
    data = response.json()

    access_token = data['access_token']
    if not access_token:
        status = 0
        return data, status
    refresh_token = data['refresh_token']

    with open('.env') as env:
        old_data = env.readlines()
        old_data[0] = f'REFRESH_TOKEN={refresh_token}' + '\n'
        env.close()

        f = open('.env', 'w')
        f.writelines(old_data)
        f.close()

    return access_token, refresh_token


result: [bytes, int] = get_camera_snapshot()
