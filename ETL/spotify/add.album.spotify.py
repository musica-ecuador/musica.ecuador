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

def spotify_artist_albums_simplified(spotifyAPI,spotify_artist_uri):
    
    #The type of the album: one of "album", "single", or "compilation". 
    #album_type - ‘album’, ‘single’, ‘appears_on’, ‘compilation’
    results = spotifyAPI.artist_albums(spotify_artist_uri, album_type='album,single,compilation')
    
    albums = results['items']
    while results['next']:
        results = spotifyAPI.next(results)
        albums.extend(results['items'])

    #tracks
    '''
    for album in albums:
        tracks = spotify_album_tracks(spotifyAPI,album)
        album['track_info'] =   tracks 
    '''

    return albums

def MapSpotifyAlbum(spotify_album):
    spotify = {}
    spotify['id'] = spotify_album['id'] 
    spotify['uri'] = spotify_album['uri'] 
    spotify['album_type'] = spotify_album['album_type'] 
    spotify['href'] = spotify_album['href'] 
    


    #other field
    return spotify


def MapArtist(spotify_albums,idArtist):
    
    artists = []

    #Artist
    if len(spotify_albums['artists'])==1:

        artists.append({
            "__type": "Pointer",
            "className": "Artist",
            "objectId": idArtist
        })

    else:
        logger.info("Album, tiene mas de un artista. Total %d" % len(spotify_albums['artists']))

        #Get Ids Spotify
        ids = []
        for spotify_artist in spotify_albums['artists']:
            ids.append(spotify_artist['id'])

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
            
            logger.info("Artists recovered: %s" % artists)  

        else:
             return None,error

    return artists,None

def InsertAlbums(idArtist,nameArtist,spotify_albums_simplified):
    
    for spotify_album in spotify_albums_simplified:

        album = {}
        album['type'] = "album"
        album['origin'] = spotify_album['external_urls']['spotify']
        album['name'] = spotify_album['name']
        album['album_type'] =spotify_album['album_type']
        
        #full album
        #album['genres'] =spotify_album['genres']
        #album['release_date']=spotify_album['release_date']
        #album['release_date_precision']=spotify_album['release_date_precision']
        
        album['images'] = spotify_album['images']
      
        result,error  =  MapArtist(spotify_album,idArtist)
        if error is not None:
            logger.error('Error al get artist from app: %s. Mensaje: %s', idArtist,error) 

        album['artists']  =  result
        
        album['spotify'] = MapSpotifyAlbum(spotify_album)

        result,error  = parse.insertParse('Album',album) 
        
        if result is not None:
            logger.info('Registro insertado: %s. ObjectId: %s', album['name'],idArtist) 
        else:
            logger.error('Error al registrar: %s. Mensaje: %s', album['name'],error) 
            

def main():

    logging.basicConfig(filename='spotify.log', level=logging.DEBUG)


    spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)

    data,error = getData() 
    
 
    if data is not None and len(data['results'])>0:

        logger.info('Procesar %d registros' % len(data))

        for item in data['results']:
            

            idArtist = item['objectId']
            nameArtist = item['name']
            spotify_artist = item['spotify']

            spotify_albums_simplified =  spotify_artist_albums_simplified(spotifyAPI,spotify_artist['uri'])

            logger.info("Insertar albunes spotify. Artista. %s" % (nameArtist))
            InsertAlbums(idArtist,nameArtist,spotify_albums_simplified)
    else:
        logger.error("Error a recuperar informacion Artistas %s" % error)   
            

if __name__ == "__main__":
    main() 
