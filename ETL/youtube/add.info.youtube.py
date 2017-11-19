from apiclient.discovery import build
import json
from pprint import pprint
import logging
import re


logger = logging.getLogger(__name__)

import sys
sys.path.append('../')

import CONFIG

import parseplatform.functions as parse


def getData():
    result = parse.getParse('Artist',"objectId,name,external_urls")
    return result

def youtube_video_channel(youtubeAPI,channel_id):

    # Call the videos.list method to retrieve video info
    resultChannel = youtubeAPI.channels().list(
        id = channel_id,
        part = "id,snippet,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    if resultChannel is not None and len(resultChannel['items']) > 0:
        video['channelId'] = resultChannel['items'][0]['id']
        video['title'] = resultChannel['items'][0]['snippet']['title']
        video['description'] = resultChannel['items'][0]['snippet']['description']
        video['stats'] = resultChannel['items'][0]['statistics']

    return video

def youtube_video_channel_forUsername(youtubeAPI,userName):

    # Call the videos.list method to retrieve video info
    resultChannel = youtubeAPI.channels().list(
        forUsername = userName,
        part = "id,snippet,statistics",
    ).execute()
    
    # Extracting required info about video
    video = {}
    if resultChannel is not None and len(resultChannel['items']) > 0:
        video['channelId'] = resultChannel['items'][0]['id']
        video['title'] = resultChannel['items'][0]['snippet']['title']
        if 'country' in resultChannel['items'][0]['snippet']:
            video['country'] = resultChannel['items'][0]['snippet']['country']
        video['description'] = resultChannel['items'][0]['snippet']['description']
        video['stats'] = resultChannel['items'][0]['statistics']

    return video


def main():
    
    logging.basicConfig(filename='youtube.log', level=logging.DEBUG)


    # creating youtube resource object for interacting with API
    youtubeAPI = build(CONFIG.YOUTUBE_API_SERVICE_NAME, CONFIG.YOUTUBE_API_VERSION,   developerKey=CONFIG.YOUTUBE_DEVELOPER_KEY)

    data,error = getData() 
 
   
    if data is not None and len(data['results'])>0:

        logger.info('Procesar %d registros' % len(data['results']))

        for item in data['results']:
            
            objectId = item['objectId']
            nameArtist = item['name']
            external_urls = item['external_urls']


            if external_urls is not None and "youtube" in external_urls:
                
                
                # Regular Expressions for url field youtube. User or Channel
                exRegUser = r'https://www.youtube.com/user/(.*)'
                exRegChannel = r'https://www.youtube.com/channel/(.*)'

                youtube_url = external_urls['youtube']
                channelInfo = None
                #Si url youtube, es el user.
                #https://www.youtube.com/user/JorgeLuisPeralta
                matchUrlUser = re.match( exRegUser, youtube_url, re.M|re.I) 
                if matchUrlUser:
                    
                    userNameYoutube =  matchUrlUser.group(1)
                    channelInfo = youtube_video_channel_forUsername(youtubeAPI,userNameYoutube)    
                
                    #update url youtube
                    external_urls['youtube'] = "https://www.youtube.com/channel/" + channelInfo['channelId']

                    resultUpdate,error = parse.updateParseField("Artist",objectId,"external_urls",external_urls)
                else:
                    #Get Info Youtube Channel
                    #https://www.youtube.com/channel/UCEm3eGhDH2W02i1VHVB4Iww
                    channel_id = youtube_url.split("/")[-1]
                    channelInfo = youtube_video_channel(youtubeAPI,channel_id)    

                resultUpdate,error = parse.updateParseField("Artist",objectId,"youtube",channelInfo)
                if error is not None:
                    logger.error("Existe un error %s, para el artista %s" % (error,nameArtist))
                    
                else:
                    logger.info("Actualizado artista %s, con informacion youtube" % (nameArtist))
                     
            
            else:
                logger.info("No existe informacion de youtube. %s" % (nameArtist))
               


if __name__ == "__main__":
    main() 