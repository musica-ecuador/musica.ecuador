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

def getData():
    result = parse.getParseExistField('Artist',"spotify","objectId,name,spotify")
    return result

def MapSpotifyAlbum(spotify_album):
    spotify = {}
    spotify['id'] = spotify_album['id'] 
    spotify['uri'] = spotify_album['uri'] 
    spotify['album_type'] = spotify_album['album_type'] 
    spotify['href'] = spotify_album['href'] 
    


    #other field
    return spotify

def main():

    logging.basicConfig(filename='spotify.log', level=logging.DEBUG)

    spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)


    data,error = getData() 
 
    if data is not None and len(data['results'])>0:

        logger.info('Procesar %d registros' % len(data['results']))

        for item in data['results']:
            
            objectId = item['objectId']
            nameArtist = item['name']
            spotify = item['spotify']

            spotifyImages = spotify['images']
           
            if (len(spotifyImages)>0):
           
                resultUpdate,error = parse.updateParseField("Artist",objectId,"images",spotifyImages)
                
                if error is not None:
                    logger.error("Existe un error %s, para el artista %s" % (error,nameArtist))
                else:
                    logger.info("Actualizado artista %s, con informacion imagenes/spotify" % (nameArtist))
          

if __name__ == "__main__":
    main() 

 