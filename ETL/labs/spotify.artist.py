
import spotipy

import sys
sys.path.append('../')

import CONFIG


 

spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

artist_uri = 'https://open.spotify.com/artist/1nV4bRtpwOUY2BAoxsLcpq'
 
results = spotifyAPI.artist(artist_uri)

print (results)
    