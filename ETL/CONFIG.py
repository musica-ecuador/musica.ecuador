

from spotipy.oauth2 import SpotifyClientCredentials


# arguments to be passed to build function


PARSE_SERVER_HTTS = 0  #1 = is https 0 = http
PARSE_SERVER =  "localhost:1337"
PARSE_APPLICATION_ID = 123 	

#spotify
spotify_client_credentials_manager = SpotifyClientCredentials(client_id = "efb1585a452d4930af31ca24ee893910",
                                   client_secret = "c28b1c21d3f54ffbbbdad1c33fc1d237")
								   
			
#youtube

from apiclient.discovery import build

# arguments to be passed to build function
YOUTUBE_DEVELOPER_KEY = "AIzaSyBHDCXMifi8vkHbcG79JIN0GlecpNkdf3c"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"		
