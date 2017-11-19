import json

import logging
logger = logging.getLogger(__name__)


import sys
sys.path.append('../')

import CONFIG

import parseplatform.functions as parse



def mapArtistSpotifyToAppSpotify(item):
 
    artist = {}
    artist['spotify'] = item['external_urls']['spotify']
    artist['followers'] = item['followers']['total']
    artist['id'] = item['id']
    artist['images'] = item['images']
    artist['genres'] = item['genres']
    artist['name'] = item['name']
    artist['popularity'] = item['popularity']
    artist['uri'] =  item['uri']
    return artist


def mapArtistSpotifyToApp(item):
    
    artist = {}
    artist['type'] = "artist"
    artist['country'] = "ec"
    artist['origin'] = item['external_urls']['spotify']

    #Format
    artist['name'] = item['name']
   
    #spotify
    artist['spotify'] = mapArtistSpotifyToAppSpotify(item)

    return artist


def mapAlbumSpotifyToAppSpotify(spotify_album):
    """
    Mapear informaction de album spotify, a la aplicacion.

    """

    album = {}
    album['id'] = spotify_album['id'] 
    album['uri'] = spotify_album['uri'] 
    album['album_type'] = spotify_album['album_type'] 
    album['href'] = spotify_album['href'] 
    
 
    #other field
    return album


def mapTrackSpotifyToAppSpotify(trackSpotify):
    spotify = {}
    spotify['id'] = trackSpotify['id'] 
    spotify['uri'] = trackSpotify['uri'] 

    #other field
    return spotify

def AppendArtistFromApp(spotify_albums,idArtist):
    """
    TODO: Mejorar nombres
    """
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


def InsertAlbumsFromSpotify(idArtist,nameArtist,spotify_albums_simplified):
    """
    """

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
      
        result,error  =  AppendArtistFromApp(spotify_album,idArtist)
        if error is not None:
            logger.error('Error al get artist from app: %s. Mensaje: %s', idArtist,error) 

        album['artists']  =  result
        
        album['spotify'] = mapAlbumSpotifyToAppSpotify(spotify_album)

        result,error  = parse.insertParse('Album',album) 
        
        if result is not None:
            logger.info('Album insertado: %s. ObjectId: %s', album['name'],idArtist) 
        else:
            logger.error('Error al registrar: %s. Mensaje: %s', album['name'],error) 


def AppendAlbum(idAlbum):
    album = {
                "__type": "Pointer",
                "className": "Album",
                "objectId": idAlbum
            }
    return album 
 
def InsertTracksFromSpotify(idAlbum,nameAlbum,artistsAlbum,spotify_tracks):
    
    """
    """

    for spotify_item in spotify_tracks:

        track = {}
        track['type'] = "track"
        track['origin'] = spotify_item['external_urls']['spotify']
        track['name'] = spotify_item['name']
        track['track_number'] = spotify_item['track_number']
        track['preview'] = spotify_item['preview_url']
        track['duration_ms'] = spotify_item['duration_ms']
         
        #TODO: other field
    
        
        result,error  =  AppendArtistFromApp(spotify_item,artistsAlbum)
        if error is not None:
            logger.info('Error al get artist from app:  Mensaje: %s', error) 

        track['artists']  =  result
        
        track['album']  =  AppendAlbum(idAlbum)
        track['spotify'] = mapTrackSpotifyToAppSpotify(spotify_item)

        result,error  = parse.insertParse('Track',track) 
        
        if result is not None:
            logger.info('Track insertado: %s. Result: %s', track['name'],result) 
        else:
            logger.info('Error al registrar: %s. Mensaje: %s', track['name'],error) 
  

def GetTrackArtist(idArtist):
    #parse/classes/Track?where={"artists":{"__type":"Pointer","className":"Artist","objectId":"8XjLFfU1ew"}}

    connection = parse.getConnection()
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    
    #generate url
    url = "/parse/classes/Track?where={\"artists\":{\"__type\":\"Pointer\",\"className\":\"Artist\",\"objectId\":\"%s\"}}" % (idArtist)
    
    try:
        connection.request('GET', url, '', headers)
        response = connection.getresponse()

        if response.status == 200:
            data = json.loads(response.read())  
            return data,None
        else:
            error = json.loads(response.read())  
            return None,error 

    except Exception as ex:
        return None,ex