import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import logging

logger = logging.getLogger(__name__)



import sys
sys.path.append('../')

import CONFIG

import parseplatform.functions as parse
import spotify.functions as spotify_custom
import app.functions as app

def getData():
    
    #Test with one artist
    #result = parse.getParseForField("Artist","objectId","GQBNOcJYgP")

    result = parse.getParseExistField('Artist',"spotify","objectId,name,spotify")
    
    
    return result

def spotify_album_tracks(spotifyAPI,album):
    tracks = []
    results = spotifyAPI.album_tracks(album['id'])
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks


def main():

    logging.basicConfig(filename='spotify.log', level=logging.DEBUG)


    spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

    data,error = getData() 
    
 
    if data is not None and len(data['results'])>0:

        logger.info('Procesar %d registros' % len(data['results']))

        for item in data['results']:
            

            idArtist = item['objectId']
            nameArtist = item['name']
            spotify_artist = item['spotify']

            spotify_albums_simplified =  spotify_custom.get_artist_albums_simplified_spotify(spotifyAPI,spotify_artist['uri'])

            logger.info("Insertar albunes spotify. Artista. %s" % (nameArtist))
            
            app.InsertAlbumsFromSpotify(idArtist,nameArtist,spotify_albums_simplified)

    else:
        logger.error("Error a recuperar informacion Artistas %s" % error)   
            

if __name__ == "__main__":
    main() 
