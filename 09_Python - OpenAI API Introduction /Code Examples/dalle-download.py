
# script that uses the OpenAI API to generate an image based on a given prompt, and then saves the generated image to a local file

import os
from dotenv import load_dotenv
from openai import OpenAI
from requests import get

# Load the .env file
load_dotenv()

# Get the OpenAI API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
openai.api_key = openai_api_key

query = 'a dog on the moon'

response = client.images.generate(
  model="dall-e-3",
  prompt=query,
  n=1,
  size="1024x1024" 
)
print(response)
print('')
print(response.created)
print('')
print(response.data[0].revised_prompt)
print('')
print(response.data[0].url)

pic_name = f'{response.created}.png' #Using Timestamp for Name

response_image = get(response.data[0].url)

with open(pic_name, 'wb') as file: #Mode 'wb' allows for writing non text files
    file.write(response_image.content) #.content is the full file from a get request