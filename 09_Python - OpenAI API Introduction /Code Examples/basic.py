
# script that interacts with the OpenAI API to generate a response to a user's message using the GPT-4 model 

# from openai import OpenAI

# client = OpenAI()

# # openai_key ='API Key from OpenAI'

# # client = OpenAI(api_key=openai_key)

# completion = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )
# print('***')
# print(completion)
# print('***')
# print(completion.choices[0].message)
# print('***')
# print(completion.choices[0].message.content)
# print(completion.usage.total_tokens)

# print(type(completion))



import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai_key = os.environ['OPENAI_API_KEY']

# Create an OpenAI client instance with the API key
client = OpenAI(api_key=openai_key)

# Rest of your script remains the same
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print('***')
print(completion)
print('***')
print(completion.choices[0].message)
print('***')
print(completion.choices[0].message.content)
print(completion.usage.total_tokens)

print(type(completion))