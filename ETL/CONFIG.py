from spotipy.oauth2 import SpotifyClientCredentials


# arguments to be passed to build function
PARSE_SERVER = "localhost:1337"
PARSE_APPLICATION_ID = "123"
 	

#spotify
spotify_client_credentials_manager = SpotifyClientCredentials(client_id = "spotify_cliente_id",
                                   client_secret = "spotify_cliente_secret")
								   
			
#youtube

from apiclient.discovery import build

# arguments to be passed to build function
YOUTUBE_DEVELOPER_KEY = "YOUTUBE_DEVELOPER_KEY"
YOUTUBE_API_SERVICE_NAME = "YOUTUBE_API_SERVICE_NAME"
YOUTUBE_API_VERSION = "YOUTUBE_API_VERSION"		