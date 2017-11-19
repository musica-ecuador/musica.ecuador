
#Function for youtube

def get_video(youtubeAPI,videoId):
    
    #Video. Part
    #id, snippet,  player,   statistics , contentDetails
    response = youtubeAPI.videos().list(
        #q=options.q,
        id=videoId,
        part='id, snippet,  player,   statistics,contentDetails' 
    ).execute()
    
    # Extracting required info about video
    video = {}
    if response is not None and len(response['items']) > 0:
        
        video['videoId'] = response['items'][0]['id']
        video['title'] = response['items'][0]['snippet']['title']
        video['description'] = response['items'][0]['snippet']['description']
        video['publishedAt'] = response['items'][0]['snippet']['publishedAt']
        video['channelId'] = response['items'][0]['snippet']['channelId']
        video['tags']  = response['items'][0]['snippet']['tags']
        video['stats'] = response['items'][0]['statistics']
        video['contentDetails'] = response['items'][0]['contentDetails'] 

    return video

def get_channed_video(youtubeAPI,channelId):
  max_results = 10

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtubeAPI.search().list(
    #q=options.q,
    channelId=channelId,
    part='id,snippet',
    maxResults=max_results
  ).execute()

  videos = []

  nextPageToken = search_response.get('nextPageToken')

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    
    if search_result['id']['kind'] == 'youtube#video':
      
      video = {
          'title': search_result['snippet']['title'],
          'videoId': search_result['id']['videoId'],
          'publishedAt':search_result['snippet']['publishedAt']
      }

      videos.append(video)
 
  while (nextPageToken is not None):
    #next page
    search_response = youtubeAPI.search().list(
      channelId=channelId,
      pageToken=nextPageToken,
      part='id,snippet'
    ).execute()

    for search_result in search_response.get('items', []):
      if search_result['id']['kind'] == 'youtube#video':
        
        video = {
          'title': search_result['snippet']['title'],
          'videoId': search_result['id']['videoId']
        }

        videos.append(video)

    nextPageToken = search_response.get('nextPageToken')

  return videos