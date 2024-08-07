
# script uses the OpenAI API to generate an image based on a given prompt using the DALL-E 3 model

import os
from dotenv import load_dotenv
from openai import OpenAI

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
  n=1, # Number of images to return. meaning only one image will be generated
  size="1024x1024" # 1024x1024
)
print(response)
print('')
print(response.created)
print('')
print(response.data[0].revised_prompt)
print('')
print(response.data[0].url)
