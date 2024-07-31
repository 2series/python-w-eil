# script response with your IP address
# in text, json format

# docs https://www.ipify.org/
# IP Geolocation API https://ip-api.com/

from requests import get

result = get('https://api.ipify.org')
print(result)
print(result.status_code)
print(result.headers)

# result_text = get('https://api.ipify.org').text
# print(result_text)

# result_json = get('https://api.ipify.org?format=json').json()
# print(result_json)

# print(result_json['ip'])