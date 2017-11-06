
import spotipy

import sys
sys.path.append('../')

import CONFIG

spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)


def spotify_album_tracks(spotifyAPI,album_spotifyId):
    tracks = []
    #Invalid limit, cannot be greater than 50
    results = spotifyAPI.album_tracks(album_spotifyId) #,limit=300)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks

album_uri = "spotify:album:0wARy8D2w46PFqXwVY9TzQ"

results = spotify_album_tracks(spotifyAPI,album_uri)
for item in results:
    print("Track: %s " % (item['name']))