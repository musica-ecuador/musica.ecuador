
import spotipy

import sys
sys.path.append('../')

import CONFIG

spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

name = "FERnando LARA"

results = spotifyAPI.search(q='artist:' + name, type='artist')

print(results)