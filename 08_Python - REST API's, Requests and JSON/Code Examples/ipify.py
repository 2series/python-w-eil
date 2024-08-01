# script REST response from source URL
# in text, json format

# docs https://www.ipify.org/
# IP Geolocation API https://ip-api.com/

from requests import get


# e.g., #1
# result = get('https://api.ipify.org')
# print(result) # response code 200
# print(result.status_code) # 200
# print(result.headers) # dict of values


# e.g., #2
# result_text = get('https://api.ipify.org').text
# print(result_text) # returns URL IP address 197.90.76.17


# e.g., #3
# result_json = get('https://api.ipify.org?format=json').json()
# print(result_json) # returns dict {'ip': '197.90.76.17'}

# print(result_json['ip']) # returns 197.90.76.17