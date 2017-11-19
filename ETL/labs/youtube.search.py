#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

 

from apiclient.discovery import build
from apiclient.errors import HttpError
import logging
from collections import namedtuple

logger = logging.getLogger(__name__)


import sys
sys.path.append('../')

import CONFIG
 

import youtube.functions as youtube_custom



if __name__ == '__main__':
 
  
  youtube = build(CONFIG.YOUTUBE_API_SERVICE_NAME, CONFIG.YOUTUBE_API_VERSION,   
        developerKey=CONFIG.YOUTUBE_DEVELOPER_KEY)

 
  result = youtube_custom.get_channed_video(youtube,'UCD9y3V_twTz-0fJmDftdoQQ')
 
  print(result)

 