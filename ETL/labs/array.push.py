 
artists = []

artista1 = {
			"__type": "Pointer",
			"className": "Artist",
			"objectId": "5TGEekLPQx"
		}

artists.append(artista1)


artista2 = {
			"__type": "Pointer",
			"className": "Artist",
			"objectId": "XnEfjkSgoU"
		}

artists.append(artista2)
artists.append('foo')
artists.append('bar')

print(artists)