
# script for web scraping, which is the process of automatically extracting data from Ars Technica

from requests import get # used to send an HTTP request to the website and retrieve its content
from bs4 import BeautifulSoup # used to parse the HTML content of the webpage

page = get('https://arstechnica.com/space/2024/08/china-deploys-first-satellites-for-a-broadband-network-to-rival-starlink/').text

soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify()) # prettify method is used to print the parsed HTML in a formatted way

# print(soup.title) # prints the title element of the webpage

# print(soup.title.text) # prints the text content of the title element

# print(soup.find_all('p')) # prints all paragraph elements on the webpage

# for line in soup.find_all('p'): # prints the text content of each paragraph element
#     print(line.text)

for line in soup.find_all('a'): # prints the URLs of all links on the webpage
    print(line.get('href'))