import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sys.path.append('../')

import CONFIG

import spotify.functions as spotify_custom


spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)


spotify_albums_simplified =  spotify_custom.get_artist_albums_simplified_spotify(spotifyAPI,"spotify:artist:1nV4bRtpwOUY2BAoxsLcpq")

print (spotify_albums_simplified)
