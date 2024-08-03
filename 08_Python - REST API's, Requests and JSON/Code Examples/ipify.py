# script uses the `requests` library to send a GET request to the [ipify API] and retrieve the user's IP address in different formats; text, json

# docs https://www.ipify.org/
# IP Geolocation API https://ip-api.com/

from requests import get


# Example 1: Retrieving the Response Object
# result = get('https://api.ipify.org')
# print(result) # response code 200
# print(result.status_code) # 200
# print(result.headers) # dict of values


# Example 2: Retrieving the IP Address as Text
result_text = get('https://api.ipify.org').text
print(result_text)


# Example 3: Retrieving the IP Address as JSON
result_json = get('https://api.ipify.org?format=json').json()
# print(result_json)

print(result_json['ip'])