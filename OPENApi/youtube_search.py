import os 
from apiclient.discovery import build
YOUTUBE_API_KEY = 'AIzaSyCBbFFUSIc6iA4qI3ymk6IwfATRw_qwsn4' 

youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    q='DEEPLEARNING',
    type='video'
).execute()

for item in search_response['items']:
    print(item['snippet']['title'])