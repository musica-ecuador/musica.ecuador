
import json
import logging
import spotipy


logger = logging.getLogger(__name__)

import sys
sys.path.append('../')

import CONFIG

import parseplatform.functions as parse
import spotify.functions as spotify_custom
import app.functions as app


def getData():
    with open('data.json') as data_file:    
        data = json.load(data_file)
    return data

 
def providerSpotify(spotifyAPI,url):

    data = spotify_custom.get_artist_spotify(spotifyAPI, url)

    if (data is  None):
        logger.error('Data no recuperada de spotify. ID: %s.', url) 
        return

    #artist
    artist = app.mapArtistSpotifyToApp(data)
    result,error  = parse.insertParse('Artist',artist) 

    if error is not None:
        logger.error('Error al registrar: %s. Mensaje: %s', artist['name'],error) 
        return 
    else:
        logger.info('Registro insertado: %s. ObjectId: %s', artist['name'],result['objectId']) 
    
    #album
    idArtist = result['objectId']
    nameArtist = artist['name']
    spotify_artist = artist['spotify']


    spotify_albums_simplified =  spotify_custom.get_artist_albums_simplified_spotify(spotifyAPI,spotify_artist['uri'])
    
    logger.info("Insertar albunes spotify. Artista. %s" % (nameArtist))

    app.InsertAlbumsFromSpotify(idArtist,nameArtist,spotify_albums_simplified)
    
    #track
    for album in spotify_albums_simplified:
        
        albumApp = None
        
        # Get Album from Ids Spotify
        ids = []
        ids.append(album['id'])
        item,error = parse.getParseInField('Album','spotify.id',ids)
        print(len(item['results']))

        if item is not None and len(item['results'])==1:
           albumApp = item['results'][0]
        else:   
            logger.error("No encontrado album %s en App" % album['name'])

        if (albumApp is not None):
            
            idAlbum = albumApp['objectId']
            nameAlbum = albumApp['name']
            artistsAlbum = albumApp['artists']
            spotify_album = albumApp['spotify']

            spotify_tracks =  spotify_custom.get_tracks_album_spotify(spotifyAPI,spotify_album['id'])

            logger.info("Insertar track spotify. Album. %s. Track Count %s" % (nameAlbum, len(spotify_tracks)))

            app.InsertTracksFromSpotify(idAlbum,nameAlbum,artistsAlbum,spotify_tracks)

def main():
    
    logging.basicConfig(filename='manual.log', level=logging.DEBUG)

    spotifyAPI = spotipy.Spotify(client_credentials_manager=CONFIG.spotify_client_credentials_manager)


    data = getData() 
 
    if data is not None and len(data)>0:
        
        logger.info('Procesar %d registros' % len(data))
        
        for item in data:
            provider = item['provider']
            url = item['url']
            
            if (provider=="spotify"):

                providerSpotify(spotifyAPI,url)
                

if __name__ == "__main__":
    main() 