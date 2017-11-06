import pprint
import spotipy

import sys
sys.path.append('../')

import CONFIG

spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)



if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:album:5yTx83u3qerZF7GRJu7eFk'


 
album = spotifyAPI.album(urn)
pprint.pprint(album['tracks'])