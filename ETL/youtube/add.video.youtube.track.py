import logging
 

logger = logging.getLogger(__name__)

import sys
sys.path.append('../')

import CONFIG

import parseplatform.functions as parse

def getData():
    result = parse.getParseExistField('Artist',"youtube","objectId,name,youtube")
    return result


def main():
    
    logging.basicConfig(filename='youtube.log', level=logging.DEBUG)

    data,error = getData() 
 
    if data is not None and len(data['results'])>0:

        logger.info('Procesar %d registros' % len(data['results']))

        for item in data['results']:
       


if __name__ == "__main__":
    main() 
