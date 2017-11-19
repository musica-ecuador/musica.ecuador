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

    #result = parse.getParseForField("Album","album_type","single")
    #result = parse.getParseForField("Album","objectId","RiFY09oc5Z")
    
    #"Beats & Notes"
    #result = parse.getParseForField("Album","objectId","6q6PsAn6HN")
  
    result = parse.getParseExistField('Album',"spotify","objectId,name,artists,spotify")

    return result


 



def MapArtist(spotify_item, artistsAlbum):
    
    artists = []

    #If one artist, is artists album
    if len(spotify_item['artists'])==1:
        artists.append(artistsAlbum)

    else:
        #Get Ids Spotify
        ids = []
        for spotify_artist in spotify_item['artists']:
            ids.append(spotify_item['id'])

        #Get Artist from Ids Spotify
        data,error = parse.getParseInField('Artist','spotify.id',ids)


        #TODO: 
        #Some artist may not exist in the app, but if it exists in spotify
        #Insert artist from Spotify

        if data is not None and len(data['results'])>0:
            for item in data['results']:
                artists.append({
                    "__type": "Pointer",
                    "className": "Artist",
                    "objectId": item['objectId']
                })
            print("Artists : %s" % artists)    
        else:
           return None,error

    return artists,None

def main():

    logging.basicConfig(filename='spotify.log', level=logging.DEBUG)


    spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

    data,error = getData() 
    
 
    if data is not None and len(data['results'])>0:
        
        logger.info("Total de Albumnes a procesar %s" % len(data['results']))

        for item in data['results']:
            
            idAlbum = item['objectId']
            nameAlbum = item['name']
            artistsAlbum = item['artists']
            spotify_album = item['spotify']
 
            spotify_tracks =  spotify_custom.get_tracks_album_spotify(spotifyAPI,spotify_album['id'])

            logger.info("Insertar track spotify. Album. %s. Track Count %s" % (nameAlbum, len(spotify_tracks)))
            
            app.InsertTracksFromSpotify(idAlbum,nameAlbum,artistsAlbum,spotify_tracks)

    else:
        logger.error("Error a recuperar informacion Albumes %s" % error)
          

if __name__ == "__main__":
    main() 