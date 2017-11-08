

from spotipy.oauth2 import SpotifyClientCredentials


# arguments to be passed to build function


PARSE_SERVER_HTTS = 0  #1 = is https 0 = http
PARSE_SERVER =  "localhost:1337"
PARSE_APPLICATION_ID = 123 	

#spotify
spotify_client_credentials_manager = SpotifyClientCredentials(client_id = "client_id",
                                   client_secret = "client_secret")
								   
			
#youtube

from apiclient.discovery import build

# arguments to be passed to build function
YOUTUBE_DEVELOPER_KEY = "YOUTUBE_DEVELOPER_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"		
