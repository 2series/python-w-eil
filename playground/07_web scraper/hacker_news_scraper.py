


# script used for web scraping, specifically designed to extract data from an article on hacker news


## E.g. 1
# from requests import get # used to send an HTTP request to the website and retrieve its content
# from bs4 import BeautifulSoup # used to parse the HTML content of the webpage

# page = get('https://scnr.com/article/ai-driven-drone-surveillance-is-leading-to-unexpected-home-insurance-cancellations_ea244cc8558f11ef9c930242ac1c0002').text

# soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify()) # prettify method is used to print the parsed HTML in a formatted way

# print(soup.title) # prints the title element of the webpage

# print(soup.title.text) # prints the text content of the title element

# print(soup.find_all('p')) # prints all paragraph elements on the webpage

# for line in soup.find_all('p'): # prints the text content of each paragraph element
    # print(line.text)

# for line in soup.find_all('a'): # prints the URLs of all links on the webpage
#     print(line.get('href'))


## E.g. 2
# script used for web scraping, specifically designed to extract data from an article on hacker news

# import requests  # used to send an HTTP request to the website and retrieve its content
# from bs4 import BeautifulSoup  # used to parse the HTML content of the webpage

# def get_page_content(url):
#     """Sends an HTTP request to the website and retrieves its content."""
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         return response.text
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None

# def parse_html(html):
#     """Parses the HTML content of the webpage."""
#     return BeautifulSoup(html, 'html.parser')

# def extract_data(soup):
#     """Extracts relevant data from the parsed HTML."""
#     title = soup.title.text
#     paragraphs = [p.text for p in soup.find_all('p')]
#     links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
#     return title, paragraphs, links

# def main():
#     url = 'https://scnr.com/article/ai-driven-drone-surveillance-is-leading-to-unexpected-home-insurance-cancellations_ea244cc8558f11ef9c930242ac1c0002'
#     html = get_page_content(url)
#     if html:
#         soup = parse_html(html)
#         title, paragraphs, links = extract_data(soup)
#         print("Title:", title)
#         print("Paragraphs:")
#         for paragraph in paragraphs:
#             print(paragraph)
#         print("Links:")
#         for link in links:
#             print(link)

# if __name__ == "__main__":
#     main()


## E.g. 3
import requests  # used to send an HTTP request to the website and retrieve its content
from bs4 import BeautifulSoup  # used to parse the HTML content of the webpage

def get_page_content(url):
    """Sends an HTTP request to the website and retrieves its content."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def parse_html(html):
    """Parses the HTML content of the webpage."""
    return BeautifulSoup(html, 'html.parser')

def extract_data(soup):
    """Extracts relevant data from the parsed HTML."""
    title = soup.title.text
    paragraphs = [p.text for p in soup.find_all('p')]
    links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
    return title, paragraphs, links

def save_to_markdown(title, paragraphs, links, filename):
    """Saves the extracted data to a Markdown file."""
    with open(filename, 'w') as f:
        f.write(f"# {title}\n\n")
        for paragraph in paragraphs:
            f.write(f"{paragraph}\n\n")
        f.write("## Links\n\n")
        for link in links:
            f.write(f"* {link}\n")

def main():
    url = 'https://scnr.com/article/ai-driven-drone-surveillance-is-leading-to-unexpected-home-insurance-cancellations_ea244cc8558f11ef9c930242ac1c0002'
    html = get_page_content(url)
    if html:
        soup = parse_html(html)
        title, paragraphs, links = extract_data(soup)
        filename = f"{title}.md"
        save_to_markdown(title, paragraphs, links, filename)
        print(f"Article saved to {filename}")

if __name__ == "__main__":
    main()