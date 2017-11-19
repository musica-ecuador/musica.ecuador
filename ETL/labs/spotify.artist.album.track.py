
import spotipy

import sys
sys.path.append('../')

import CONFIG


def album_tracks(spotifyAPI,album):
    tracks = []
    results = spotifyAPI.album_tracks(album['id'])
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks


spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

artist_uri = 'spotify:artist:3vA0UcLmHZEoVavifm65mc'
artist_uri = 'https://open.spotify.com/artist/7hI5M3PWRvRznwqOXq4OIk'
 
results = spotifyAPI.artist_albums(artist_uri, album_type='album,single,compilation')
albums = results['items']
while results['next']:
    results = spotifyAPI.next(results)
    albums.extend(results['items'])

#tracks
for album in albums:
    tracks = album_tracks(spotifyAPI,album)
    album['track_info'] =   tracks 

#print
for album in albums:
    print("Album: %s tipo: %s uri: %s" % (album['name'],album['album_type'],album['uri']))
    print()
    print("     track")
    print()
    for track in album['track_info']:
        print("     Track: %s " % (track['name']))
    
    print()
    print()
    