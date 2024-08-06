# script that scrapes tech news articles from Ars Technica and stores them in a SQLite database

import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_arstechnica():
    """Scrapes tech news from Arstechnica and stores it in a database."""

    url = 'https://arstechnica.com'
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('li', class_='article')

    conn = sqlite3.connect('data/arstechnica_news.db') 
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            url TEXT UNIQUE,
            summary TEXT 
        )
    ''')

    for article in articles:
        title_elem = article.find('h2', class_='article-title')
        title = title_elem.text.strip() if title_elem else "N/A"

        url_elem = article.find('a')  
        url = url_elem['href'] if url_elem else "N/A"

        summary_elem = article.find('p')  
        summary = summary_elem.text.strip() if summary_elem else "N/A"
        
        try:
            cursor.execute(
                "INSERT INTO articles (title, url, summary) VALUES (?, ?, ?)", 
                (title, url, summary)
            )
        except sqlite3.IntegrityError:
            print(f"Skipping duplicate article: {title}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    scrape_arstechnica()