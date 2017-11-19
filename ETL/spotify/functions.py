
def get_artist_albums_simplified_spotify(spotifyAPI,spotify_artist_uri):
    """
    Get Information Albums of Artist form Spotify
    """

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


def get_artist_spotify(spotifyAPI,artist_uri):
    results = spotifyAPI.artist(artist_uri)
    return results


def get_tracks_album_spotify(spotifyAPI,album_spotifyId):
    tracks = []
    #Invalid limit, cannot be greater than 50
    results = spotifyAPI.album_tracks(album_spotifyId) #,limit=300)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks
