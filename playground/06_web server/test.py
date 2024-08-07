

# script uses the requests library to send an HTTP GET request to a specified URL and prints out the response details

import requests

try:
    response = requests.get('http://aosabook.org/en/500L/web-server/testpage.html', timeout=5)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
except requests.RequestException as e:
    print(f"Request failed: {e}")
else:
    print('status code:', response.status_code)
    if 'content-length' in response.headers:
        print('content length:', response.headers['content-length'])
    if response.headers['content-type'].startswith('text'):
        print(response.text)
    else:
        print("Non-text response content")