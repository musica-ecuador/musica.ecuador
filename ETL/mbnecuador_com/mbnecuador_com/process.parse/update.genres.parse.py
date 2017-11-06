import http.client
import json
import logging
import urllib 

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append('../')

import parseplatform.functions as parse


def getData():
    with open('_out/artistas.json') as data_file:    
        data = json.load(data_file)
    return data

  

def main():
     
    logging.basicConfig(filename='parse.log', level=logging.DEBUG)

    data = getData()
    
    logger.info('Procesar %d registros' % len(data))

    for item in data:
        name_artist = item['nombre']
        genre = item['categoria']
        
        #TODO: Process name duplica
        #data,error = parse.getParseTextSearch("Artist","name",name_artist)
        data,error = parse.getParseForField("Artist","name",name_artist)
    
        genres = [genre]
    
        if data is not None and len(data['results'])==1:
            
            objectId = data['results'][0]['objectId']
            result,error = parse.updateParseField("Artist",objectId,"genres",genres)
            
            if error is not None:
                logger.error("Existe un error %s, para el artista %s" % (error,name_artist))
            else:
                logger.info("Actualizado artista %s" % (name_artist))
        else:
            logger.error("El nombre del artista {0}, no existe o existe mas de una coindicencia".format(name_artist))


def test_search():
    
    data,error = parse.getParseTextSearch("Artist","name","STAR SQssUADx")
  

    if data is not None and len(data['results'])==1:
        print (data)
    else:
        print (error)

if __name__ == "__main__":
    main() 
