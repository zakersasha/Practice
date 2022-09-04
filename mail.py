import requests

MAIL_CLIENT_ID = '77fdb07947264df484c09570c32381ba'
MAIL_CLIENT_SECRET = '70914e37cd584fa7aab242a77e0abc59'
code = '0256771812047389a2c651667325f1fd6b7b239337363830'

import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}


data = f'grant_type=authorization_code&code={code}'

r = requests.post('https://o2.mail.ru/token', headers=headers, data=data,
                  auth=(MAIL_CLIENT_ID, MAIL_CLIENT_SECRET))
print(r.json())
token = r.json()['access_token']

params = {
    'access_token': token,
}

r = requests.get('https://oauth.mail.ru/userinfo', params=params)
user_data = r.json()

email = user_data['email']
first_name = user_data['first_name']
last_name = user_data['last_name']
