
# script retrieves the HTML content of the Hacker News website (https://news.ycombinator.com/) using the requests library in Python and saves it to a local file named hn.html

## basic example
# from requests import get

# res = get('https://news.ycombinator.com/').text    

# print(res)
# with open('hn.html', 'w') as file:
#     file.write(res)



## example 2
# import requests
# from bs4 import BeautifulSoup

# def retrieve_hn_html(url: str, output_file: str) -> None:
#     """
#     Retrieves the HTML content of the Hacker News website and saves it to a local file.

#     Args:
#         url (str): The URL of the Hacker News website.
#         output_file (str): The name of the output file.

#     Returns:
#         None
#     """
#     try:
#         # Send a GET request to the Hacker News website
#         response = requests.get(url)

#         # Check if the request was successful
#         if response.status_code == 200:
#             # Get the HTML content of the page
#             html_content = response.text

#             # Parse the HTML content using BeautifulSoup
#             soup = BeautifulSoup(html_content, 'html.parser')

#             # Write the HTML content to a file
#             with open(output_file, 'w', encoding='utf-8') as file:
#                 file.write(soup.prettify())

#             print(f"HTML content saved to {output_file}")
#         else:
#             print(f"Failed to retrieve HTML content. Status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     url = 'https://news.ycombinator.com/'
#     output_file = 'hn2.html'
#     retrieve_hn_html(url, output_file)


## example 3
import requests
from bs4 import BeautifulSoup
import sqlite3

def retrieve_hn_html(url: str, output_file: str, db_name: str) -> None:
    """
    Retrieves the HTML content of the Hacker News website, saves it to a local file, and saves it to an SQLite database.

    Args:
        url (str): The URL of the Hacker News website.
        output_file (str): The name of the output file.
        db_name (str): The name of the SQLite database.

    Returns:
        None
    """
    try:
        # Send a GET request to the Hacker News website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the HTML content of the page
            html_content = response.text

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Write the HTML content to a file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(soup.prettify())

            print(f"HTML content saved to {output_file}")

            # Connect to the SQLite database
            conn = sqlite3.connect(db_name)
            c = conn.cursor()

            # Create a table to store the HTML content if it doesn't exist
            c.execute('''
                CREATE TABLE IF NOT EXISTS hn_html
                (id INTEGER PRIMARY KEY, html_content TEXT)
            ''')

            # Insert the HTML content into the table
            c.execute('INSERT INTO hn_html (html_content) VALUES (?)', (soup.prettify(),))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            print(f"HTML content saved to {db_name}")
        else:
            print(f"Failed to retrieve HTML content. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def retrieve_html_from_db(db_name: str) -> str:
    """
    Retrieves the HTML content from the SQLite database.

    Args:
        db_name (str): The name of the SQLite database.

    Returns:
        str: The HTML content.
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('SELECT html_content FROM hn_html ORDER BY id DESC LIMIT 1')
    html_content = c.fetchone()[0]

    conn.close()

    return html_content

if __name__ == "__main__":
    url = 'https://news.ycombinator.com/'
    output_file = 'hn3.html'
    db_name = 'hn.db'

    retrieve_hn_html(url, output_file, db_name)

    html_content = retrieve_html_from_db(db_name)
    print(html_content)