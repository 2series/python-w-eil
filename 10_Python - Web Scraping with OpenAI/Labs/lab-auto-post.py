

# script is designed to automate the process of creating a blog post based on a given URL. It uses web scraping to extract text from the URL, OpenAI's GPT-4 model to generate a blog post based on the extracted text, and OpenAI's DALL-E 3 model to generate an image related to the blog post

import os
from dotenv import load_dotenv
from requests import get
from bs4 import BeautifulSoup
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai_key = os.environ['OPENAI_API_KEY']

# Create an OpenAI client instance with the API key
client = OpenAI(api_key=openai_key)

def scrape(url):
    page = get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    post = soup.find_all('p')
    text =''
    for line in post: #Create a string without HTML tags
        text = f'{text} {line.text}'
    return text

def ai(query):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a blogger."},
        {"role": "user", "content": f"Create a 200 word blod post about -- {query}"},
        {"role": "user", "content": f"Do not mention author"},
        {"role": "user", "content": f"Do not mention when post was written"},
    ]
    )
    response = completion.choices[0].message.content
    return response

def ai_image(query):
    response = client.images.generate(
        model="dall-e-3",
        prompt=query,
        n=1,
        size="1792x1024" 
    )
    
    pic_name = f'{response.created}.png' #Using Timestamp for Name
    response_image = get(response.data[0].url)
    with open(pic_name, 'wb') as file: #Mode 'wb' allows for writing non text files
        file.write(response_image.content) #.content is the full file from a get request

    return pic_name

url = 'https://arstechnica.com/space/2024/08/china-deploys-first-satellites-for-a-broadband-network-to-rival-starlink/'
query = 'provide a 20 word summary'
result_bs = scrape(url)
result_ai = ai(result_bs)
pic_name = ai_image(result_ai)

with open('auto-post.html', 'a') as file:
    file.write(f'<img style="height:300px; width:auto;" src="{pic_name}">')
    file.write(f'<p>{result_ai}</p>')

print(pic_name)
print(result_ai)