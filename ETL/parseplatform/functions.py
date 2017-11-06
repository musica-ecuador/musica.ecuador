import http.client
import json
import urllib 
import re

import sys
sys.path.append('../')

import CONFIG 

def getConnection():
    if CONFIG.PARSE_SERVER_HTTS == 1:
        connection = http.client.HTTPSConnection(CONFIG.PARSE_SERVER) #, 443)
    else:
        connection = http.client.HTTPConnection(CONFIG.PARSE_SERVER) #, 443)
    return connection


def string_delete_whitespace(value):
    valor_format  = re.sub(' +',' ',value.strip())
    return valor_format 

def insertParse(class_name,data):

    connection = getConnection()
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    json_data = json.dumps(data)
     
  
    url = "/parse/classes/{0}".format(class_name)

    try:

        connection.request('POST', url, json_data, headers)
        response = connection.getresponse()
    
        if response.status == 200 or response.status == 201:
            data = json.loads(response.read())  
            return data,None
        else:
            print(response.status)
            error = json.loads(response.read())  
            return None,error 
    
    except Exception as ex:
        return None,ex

 
def getParseInField(class_name,field,ids):
    connection = getConnection()
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    #params
    params = {}
    params[field] = {"$in":ids}
  
    #encode
    value = urllib.parse.quote(json.dumps(params))

    #generate url
    url = "/parse/classes/%s?where=%s" % (class_name,value)
    url = string_delete_whitespace(url)
    print(url)

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

def getParseForField(class_name,field,value):
    connection = getConnection()
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
    connection = getConnection()
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

def getParseExistField(class_name,fieldExists,fields):
    connection = getConnection()
    
    headers = {
                'Content-type': 'application/json', 
                "X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID, 
              } 

    where = "where={\"%s\":{\"$exists\":true}}" % fieldExists
    print(where)

    params = urllib.parse.urlencode({"where":{"%s" % fieldExists:{"$exists":"true"}}})
 
    #generate url
    url = "/parse/classes/%s?%s&keys=%s&limit=%d" % (class_name,where,fields,1000)
    print(url)
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
    connection = getConnection()
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
    
    connection = getConnection()
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

      