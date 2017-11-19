#Spotify
#{"url":"https://open.spotify.com/artist/7hI5M3PWRvRznwqOXq4OIk","provider":"spotify"},

#Youtube
#https://www.youtube.com/channel/UCOU67jVqYJ-pps80nfWIEvw

#App. Parse
#"objectId": "8XjLFfU1ew",

from apiclient.discovery import build			
import sys
sys.path.append('../')

import CONFIG

import app.functions as app
import youtube.functions as youtube_custom


 
 
  
#ap
result = app.GetTrackArtist("8XjLFfU1ew")
print(result)


#youtube
youtube = build(CONFIG.YOUTUBE_API_SERVICE_NAME, CONFIG.YOUTUBE_API_VERSION,   
    developerKey=CONFIG.YOUTUBE_DEVELOPER_KEY)

result = youtube_custom.get_channed_video(youtube,'UCOU67jVqYJ-pps80nfWIEvw')

print(result)