
# script retrieves the transcript of a YouTube video using the YouTube Transcript API, and then uses the OpenAI API to analyze the transcript and answer a user-provided query


import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai_key = os.environ['OPENAI_API_KEY']

# Create an OpenAI client instance with the API key
client = OpenAI(api_key=openai_key)

def transcript(video_id):
    script = YouTubeTranscriptApi.get_transcript(video_id)
    return script

def ai(query, text):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"provide answer from this document {text}"},
        {"role": "user", "content": query}
    ]
    )
    response = completion.choices[0].message.content
    return response

video_id = '6Zl8vBkKAWQ'
query = 'Tell me what general sections there are in this video'

result_text = transcript(video_id)
result_ai = ai(query, result_text)

print(result_ai)