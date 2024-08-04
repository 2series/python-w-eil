
# script uses the `requests` library to send a GET request to the website [Ars Technica] and prints the HTML response in text format

# When you run this script, you should see the HTML content of the Ars Technica homepage printed to the console. This will include the HTML structure, CSS styles, and JavaScript code that make up the webpage

from requests import get

response = get('http://www.arstechnica.com').text

print(response)