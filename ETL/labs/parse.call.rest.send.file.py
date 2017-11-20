import requests
import json

import sys
sys.path.append('../')

import CONFIG

#Post
url = 'http://localhost:1337/parse/classes/Foo'
payload = {'some': 'directo',
            'nivel3': { 
                "foo":"bar","x":"value"
                }
           }

headers = {"X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID}

#resp = requests.post(url, data=payload, headers=headers)
#resp = requests.post(url, data=json.dumps(payload), headers=headers)
resp = requests.post(url, json=payload, headers=headers) 
#resp = requests.post(url, json=json.dumps(payload), headers=headers) 


data = json.loads(resp.text)
print(resp)
print(resp.status_code)
print(data)
 

#Post File
data = open('imagen.bar.jpg', 'rb').read()

headers = {"X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID,'Content-Type': 'image/jpeg'}

resp = requests.post(url='http://localhost:1337/parse/files/imgen.jpg',
                    data=data,
                    headers=headers)

if (resp.status_code == 201):
    print("Archivo Subido...")

    data = json.loads(resp.text)
    url = data["url"]
    name = data["name"]

    #asociar archivo a un objeto
    url = 'http://localhost:1337/parse/classes/Categoria'
    payload = {
          "some": "bar",
          "picture2": {
            "url": url,
            "name": name,
            "__type": "File"
         }
    }
    print(json.dumps(payload))

    headers = {"X-Parse-Application-Id": CONFIG.PARSE_APPLICATION_ID}

    resp = requests.post(url,  json=payload, headers=headers)

    data = json.loads(resp.text)
    print("Archivo Asociado...")
    print(resp.status_code)
    print(data)
