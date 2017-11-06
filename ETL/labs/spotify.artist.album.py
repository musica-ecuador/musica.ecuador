
import spotipy

import sys
sys.path.append('../')

import CONFIG

spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)


artist_uri = 'spotify:artist:6mwBayLYukgb8S1Af0fndm'
 
#The type of the album: one of "album", "single", or "compilation". 
#album_type - ‘album’, ‘single’, ‘appears_on’, ‘compilation’

results = spotifyAPI.artist_albums(artist_uri,'album,single,compilation')
albums = results['items']
while results['next']:
    results = spotifyAPI.next(results)
    albums.extend(results['items'])

for album in albums:
    print("Album: %s tipo: %s uri: %s" % (album['name'],album['album_type'],album['uri']))