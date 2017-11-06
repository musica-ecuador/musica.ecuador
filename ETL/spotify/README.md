General.
Todos los procesos generan logs en archivo spotify.log

1. Ejecutar Proceso Asociar informacion de Spotify al registro de artistas existentes

    update.artist.from.spotify
    
    run folder spotify

    TODO: Al momento de buscar el nombre del artista en spotify, puede exister mas de un resultado
    dos artistas de diferentes nacionalidades. 


2. Ejecutar Proceso para recuperar albums de spotify, de los artistas que tenga asociada 
   informacion de spotify

    add.album.spotify.py
    
    run folder spotify

3. Ejecutar proceso para recuperar track de spotify, de los artistas que tenga asociada
   informacion de spotify / albums

    add.track.spotify.py
    run folder spotify

4. Ejecutar proceso para asociar las imagenes de spotify, en las imagenes de artistas. 

    update.images.artist.from.spotify.py
    run folder spotify