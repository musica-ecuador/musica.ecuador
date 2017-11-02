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
    result = parse.getParse('Artist',"objectId,name")
    return result

def mapSpotifyArtist(data):
    
    total = data['artists']['total']
    #if exit one result
    if total==1:
        artist = {}
        item = data['artists']['items'][0]
        artist['spotify'] = item['external_urls']['spotify']
        artist['followers'] = item['followers']['total']
        artist['id'] = item['id']
        artist['images'] = item['images']
        artist['genres'] = item['genres']
        artist['name'] = item['name']
        artist['popularity'] = item['popularity']
        artist['uri'] =  item['uri']
        return artist

    return None

def getSpotifyInfo(spotifyAPI,name):
    #search artist for name
    results = spotifyAPI.search(q='artist:' + name, type='artist')
    return mapSpotifyArtist(results)

def main():

    spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

    data,error = getData() 
    
 
    if data is not None and len(data['results'])>0:

        for item in data['results']:
            

            objectId = item['objectId']
            nameArtist = item['name']

            spotifyData =  getSpotifyInfo(spotifyAPI,nameArtist)

            if spotifyData is not None:

                resultUpdate,error = parse.updateParseField("Artist",objectId,"spotify",spotifyData)
                
                if error is not None:
                    print("Existe un error %s, para el artista %s" % (error,nameArtist))
                else:
                    print("Actualizado artista %s, con informacion spotify" % (nameArtist))
          
            else:
                print("No existe informacion de spotify. %s" % (nameArtist))
            
    
if __name__ == "__main__":
    main() 

 