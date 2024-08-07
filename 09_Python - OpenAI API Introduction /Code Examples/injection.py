
# script uses the OpenAI API to interact with different GPT models and retrieve answers to a specific question

# from openai import OpenAI

# client = OpenAI()

# query = 'what are the national political parties'

# injection = 'france'

# gpt_model = ['gpt-4o', 'gpt-4o-mini', 'gpt-4', 'gpt-3.5-turbo']

# for version in gpt_model:
#     completion = client.chat.completions.create(
#     model=version,
#     messages=[
#         {"role": "system", "content": "You Provide Answers to Question."},
#         {"role": "user", "content": f"I am from {injection}"},
#         {"role": "user", "content": "Answer in 10 words or less"},
#         {"role": "user", "content": query}
#     ]
#     )
#     print(version)
#     print(completion.choices[0].message.content)



import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

# Get the OpenAI API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
openai.api_key = openai_api_key

query = 'what are the national political parties'
injection = 'france'

gpt_model = ['gpt-4o', 'gpt-4o-mini', 'gpt-4', 'gpt-3.5-turbo']

for version in gpt_model:
    completion = client.chat.completions.create(
        model=version,
        messages=[
            {"role": "system", "content": "You Provide Answers to Question."},
            {"role": "user", "content": f"I am from {injection}"},
            {"role": "user", "content": "Answer in 10 words or less"},
            {"role": "user", "content": query}
        ]
    )
    print(version)
    print(completion.choices[0].message.content)