import http.client
import json
import urllib 

PARSE_SERVER = "localhost:1337"
PARSE_APPLICATION_ID = "123"
 	

connection = http.client.HTTPConnection(PARSE_SERVER) #, 443)
headers = {
            'Content-type': 'application/json', 
            "X-Parse-Application-Id": PARSE_APPLICATION_ID, 
            } 

query = {}


name = urllib.parse.quote("STAR SQUAD")
term = {}
term["$term"] = name

search = {}
search["$search"] = term

text = {}
text["$text"] = search

query["name"] = text

str_query = json.dumps(query)
#str_query = urllib.parse.quote(str_query)
print(str_query)

url = "/parse/classes/%s?where=%s" % ("Artist",str_query)
#url = urllib.parse.quote(url)
print(url)



url = "/parse/classes/Artist?where={\"name\":{\"$text\":{\"$search\":{\"$term\":\"%s\"}}}}" % (name)

connection.request('GET', url, '', headers)
response = connection.getresponse()

result = json.loads(response.read())  

print(result)
