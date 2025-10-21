
from fastapi import FastAPI
import os
from dotenv import load_dotenv
import requests
import json
from videoIdExtractor import extractVideoId
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()
app = FastAPI()
RECIPIES = [{'title':'title 1', 'ingredients':['salt', 'water', 'egg'],'procedure':'loremipsumkdfjhkdjf sdufhvdkjfv'}]

@app.get("/recipies")
async def read_all_recipe():
    return RECIPIES

@app.get("/recipe/{recipe_title}")
async def read_recipe(book_title: str):
    for recipe in RECIPIES:
        if recipe.get('title').casefold() == book_title.casefold():
            return recipe
        
@app.post("/recipe/generate_recipe")
async def generate_recipe(link: str):

    API_KEY = os.getenv("YOUTUBE_API_KEY")

    # extract video id from link
    VIDEO_ID = extractVideoId(link)
    if not VIDEO_ID:
        return {"error": "Could not extract video ID from the provided link."}
    
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={VIDEO_ID}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
   # Extract description
    if 'items' in data and len(data['items']) > 0:
        description = data['items'][0]['snippet']['description']
        title = data['items'][0]['snippet']['title']
    
        # Extract transcript
        # transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
        # for entry in transcript:
        #     print(entry['text'])

        RECIPIES.append({
            'title': title,
            'procedure': description,
            # 'transcript': transcript,
        })
        return {
            'message': 'recipe generated successfully',
            'response':data
        }
    else:
       return "Video not found or error occurred"
        
    