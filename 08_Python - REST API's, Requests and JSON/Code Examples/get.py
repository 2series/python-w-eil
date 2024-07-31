# script returns web page response html, css
# get request method in text format

from requests import get

response = get('http://www.arstechnica.com').text

print(response)