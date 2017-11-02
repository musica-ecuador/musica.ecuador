import http.client
import json
import urllib 

import logging

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import function_parse as parse


def getData():
    with open('_out/artistas.json') as data_file:    
        data = json.load(data_file)
    return data

  

def main():
     
    data = getData()

    for item in data:
        name_artist = item['nombre']
        genre = item['categoria']
        
        #data,error = parse.getParseTextSearch("Artist","name",name_artist)
        data,error = parse.getParseForField("Artist","name",name_artist)
    
        genres = [genre]
    
        if data is not None and len(data['results'])==1:
            
            objectId = data['results'][0]['objectId']
            result,error = parse.updateParseField("Artist",objectId,"genres",genres)
            
            if error is not None:
                print("Existe un error %s, para el artista %s" % (error,name_artist))
            else:
                print("Actualizado artista %s" % (name_artist))
        else:
            print("El nombre del artista {0}, no existe o existe mas de una coindicencia".format(name_artist))
        
def test_search():
    
    data,error = parse.getParseTextSearch("Artist","name","STAR SQssUADx")
  
    if data is not None and len(data['results'])==1:
        print (data)
    else:
        print (error)

if __name__ == "__main__":
    main() 
