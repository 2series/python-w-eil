
# script retrieves the transcript of a YouTube video using the youtube_transcript_api library and prints the transcript to the console

# install the youtube_transcript_api library using pip: pip install youtube_transcript_api

from youtube_transcript_api import YouTubeTranscriptApi

video_id = '6Zl8vBkKAWQ'

script = YouTubeTranscriptApi.get_transcript(video_id)


# prints the entire transcript to the console
# print(script)

# loop iterates over each line in the transcript and prints the text of each line to the console
for line in script:
    print(line['text'])