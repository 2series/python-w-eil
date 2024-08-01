# script respond output dict format
# dumps module Response is prettier

from requests import get
from json import dumps

ip = '151.101.3.5' #cnn.com

result = get(f'http://ip-api.com/json/{ip}').json()

# print(result) # response dict of values
# print(result['city']) # response San Francisco

print(dumps(result, indent=2))