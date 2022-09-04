import requests

"""1) Переходим на https://api.ivideon.com/auth/oauth/authorize?client_id=samoletgroup&response_type=code 
   2) Нажимаем разрешить и копируем код из url
   3) Вставляем код в data 'code' 
"""

data = {
    'client_id': 'partner',
    'client_secret': 'ENt4unQG6',
    'grant_type': 'authorization_code',
    'code': '100-8cfb8de2c945411dbd18aab137750b1a',
    'redirect_uri': 'https://center.samoletgroup.ru/api/v1/ivideon',
}

response = requests.post('https://api.ivideon.com/auth/oauth/token', data=data)
data = response.json()
access_token = data['access_token']
refresh_token = data['refresh_token']
print(refresh_token, access_token)
