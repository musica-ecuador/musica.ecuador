1. Ejecutar:  

    Direct Folder spiders:
    scrapy runspider mbnecuador_spider.py -o _out/artistas.json 
   
    Root  Project
    scrapy crawl Mbnecuador -o _out/artistas.json 


    Este proceso extrae informacion  del sitio web "mbnecuador.com" de artistas ecuatorianos
    La salida de este proceso "artistas.json", se utilizan en el siguiente proceso

2. Ejecutar: 

    Direct Folder spiders:
    scrapy runspider mbnecuador_individual_spider.py -o artistas_details.json 

    Root  Project
    scrapy crawl MbnecuadorIndividual -o _out/artistas_details.json 
    

   Este proceso extrae informacion  del sitio web "mbnecuador.com" de artistas ecuatorianos
   La salida de este proceso "artistas_details.json", se utilizan en el siguiente proceso

3. Ejecutar:

    Root Project
    python.exe mbnecuador_com\process.parse\insert.data.parse.py

   Este proceso inserta informacion con parseplataform
   
   
4. Ejecutar:

    Root Project
    python.exe mbnecuador_com\process.parse\update.genres.parse.py

   Este proceso actualiza los generos obtenidos desde mbecuador

5. TODO: PROCESAR DUPLICADOS (NOMBRES)