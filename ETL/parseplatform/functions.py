import http.client
import json
import urllib 

import sys
sys.path.append('../')

import CONFIG 




def insertParse(class_name,data):

    connection = http.client.HTTPConnection(CONFIG.PARSE_SERVER) #, 443)
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    json_data = json.dumps(data)
     
  
    url = "/parse/classes/{0}".format(class_name)

    try:

        connection.request('POST', url, json_data, headers)
        response = connection.getresponse()
    
        if response.status == 200:
            data = json.loads(response.read())  
            return data,None
        else:
            error = json.loads(response.read())  
            return None,error 
    
    except Exception as ex:
        return None,ex


def getParseForField(class_name,field,value):
    connection = http.client.HTTPConnection(CONFIG.PARSE_SERVER) #, 443)
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    #encode
    value = urllib.parse.quote(value)

    #generate url
    url = "/parse/classes/%s?where={\"%s\":\"%s\"}" % (class_name,field,value)
   
    try:
        connection.request('GET', url, '', headers)
        response = connection.getresponse()

        if response.status == 200:
            data = json.loads(response.read())  
            return data,None
        else:
            error = json.loads(response.read())  
            return None,error 

    except Exception as ex:
        return None,ex

def getParse(class_name,fields):
    connection = http.client.HTTPConnection(CONFIG.PARSE_SERVER) #, 443)
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    
    #generate url
    url = "/parse/classes/%s?limit=%d&keys=%s" % (class_name,1000,fields)
    
    try:
        connection.request('GET', url, '', headers)
        response = connection.getresponse()

        if response.status == 200:
            data = json.loads(response.read())  
            return data,None
        else:
            error = json.loads(response.read())  
            return None,error 

    except Exception as ex:
        return None,ex

def getParseTextSearch(class_name,field,value):
    connection = http.client.HTTPConnection(CONFIG.PARSE_SERVER) #, 443)
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    #encode
    value = urllib.parse.quote(value)

    #generate url
    url = "/parse/classes/%s?where={\"%s\":{\"$text\":{\"$search\":{\"$term\":\"%s\"}}}}" % (class_name,field,value)
   
    try:
        connection.request('GET', url, '', headers)
        response = connection.getresponse()

        if response.status == 200:
            data = json.loads(response.read())  
            return data,None
        else:
            error = json.loads(response.read())  
            return None,error 

    except Exception as ex:
        return None,ex



def updateParseField(class_name,objectId,field,newValue):
    
    connection = http.client.HTTPConnection(CONFIG.PARSE_SERVER) #, 443)
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    data = {}
    data[field] = newValue
    json_data = json.dumps(data)
      

    url = "/parse/classes/{0}/{1}".format(class_name,objectId)

    try:
        connection.request('PUT', url, json_data, headers)
        response = connection.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read())  
            return data,None
        else:
            error = json.loads(response.read())  
            return None,error
    
    except Exception as ex:
        return None,ex         

      