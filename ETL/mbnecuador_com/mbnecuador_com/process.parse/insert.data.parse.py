import http.client
import json
import logging

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append('../')

import parseplatform.functions as parse

def getData():
    with open('_out/artistas_details.json') as data_file:    
        data = json.load(data_file)
    return data


def main():
    
    logging.basicConfig(filename='parse.log', level=logging.DEBUG)

    data = getData()

    logger.info('Procesar %d registros' % len(data))
    
    for item in data:
        artist = {}
        artist['type'] = "artist"
        artist['origin'] = item['url']

        #Format
        artist['name'] = item['nombre']
        artist['country'] = "ec"

        external_urls = {}
        if item['facebook'] is not None:
           external_urls['facebook'] = item['facebook']
        
        if item['youtube'] is not None:
            external_urls['youtube'] = item['youtube']

        if item['instagram'] is not None:
            external_urls['instagram'] = item['instagram']   

        if item['twitter'] is not None:
            external_urls['twitter'] = item['twitter']   

        artist['external_urls'] = external_urls

        result,error  = parse.insertParse('Artist',artist) 
        
        if error is not None:
           logger.error('Error al registrar: %s. Mensaje: %s', item['nombre'],error) 
        else:
           logger.info('Registro insertado: %s. ObjectId: %s', item['nombre'],result['objectId']) 


if __name__ == "__main__":
    main() 

         

