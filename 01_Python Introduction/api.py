import requests

result = requests.get('http://ip-api.com/json/24.48.0.1').json()

print(result)

print('CITY:')
print(result['city'])