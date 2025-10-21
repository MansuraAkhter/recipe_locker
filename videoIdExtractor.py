# for youtube
import re
from urllib.parse import urlparse, parse_qs

def extractVideoId(url):
    """
    Extract video ID from various YouTube URL formats.
    
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/shorts/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://m.youtube.com/watch?v=VIDEO_ID
    """
    
    # Method 1: Using regex (most reliable for all formats)
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/shorts\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    # Method 2: Using URL parsing (backup method)
    # try:
    #     parsed_url = urlparse(url)
        
    #     # Handle /watch?v= format
    #     if parsed_url.path == '/watch':
    #         query_params = parse_qs(parsed_url.query)
    #         if 'v' in query_params:
    #             return query_params['v'][0]
        
    #     # Handle /shorts/, /embed/, youtu.be/ formats
    #     path_parts = parsed_url.path.split('/')
    #     if len(path_parts) > 1:
    #         video_id = path_parts[-1]
    #         # Validate it looks like a video ID (11 characters)
    #         if len(video_id) == 11:
    #             return video_id
    # except:
    #     pass
    
    # return None


# Test with your URL
test_urls = [
    "https://www.youtube.com/shorts/-r-ukr0wjLA",
    "https://www.youtube.com/watch?v=-r-ukr0wjLA",
    "https://youtu.be/-r-ukr0wjLA",
    "https://www.youtube.com/embed/-r-ukr0wjLA",
    "https://m.youtube.com/watch?v=-r-ukr0wjLA",
]

print("Testing Video ID Extraction:\n")
for url in test_urls:
    video_id = extractVideoId(url)
    print(f"URL: {url}")
    print(f"Video ID: {video_id}\n")


# Simple one-liner for your specific case
# url = "https://www.youtube.com/shorts/-r-ukr0wjLA"
# video_id = url.split('/')[-1].split('?')[0]
# print(f"Quick extraction: {video_id}")