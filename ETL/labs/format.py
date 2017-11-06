
import re
import json
import http.client
import urllib 

def format_string_strip(value):
    valor_format  = value.strip()
    return valor_format


def format_string_exp(value):
    valor_format  = re.sub(' +',' ',value)
    return valor_format
 
def format_string(value):
    valor_format  = re.sub(' +',' ',value.strip())
    return valor_format 

print('Format strip:')
print(format_string_strip(' Hello '))
print(format_string_strip('Espacios al final '))
print(format_string_strip('    Espacios al inicio '))
print(format_string_strip('Espacios              entre             palabras'))


print('Format expresion regular:')
print(format_string_exp(' Hello '))
print(format_string_exp('Espacios al final '))
print(format_string_exp('    Espacios al inicio '))
print(format_string_exp('Espacios              entre             palabras'))


print('Format final:')
print(format_string(' Hello '))
print(format_string('Espacios al final '))
print(format_string('    Espacios al inicio '))
print(format_string('Espacios              entre             palabras'))



variable = 'foo'

texto = "el valor de la variable : {0}".format(variable)


print (texto)


def convertString(array):
    str = "["
     
    return str

ids = []
ids.append("foo")
ids.append("bar")

values = {"$in":ids}

field = "spotify.id"
params = {}
params[field] = {"$in":ids}

#generate url
url = "/parse/classes/%s?where={\"%s\":{\"$in\":%s}}" % ('Album',"spotify.id",ids)

print(url)

url2 = json.dumps(ids)
print(url2)

url3 = json.dumps(params)
print(url3)

url4 = "/parse/classes/%s?where=%s" % ('Album',url3)
print(url4)


twoWorlds = json.dumps("two worlds")
print(twoWorlds)


id = "mhjR7AnJjL"
#encode
value = urllib.parse.quote(id)
print(value)

#encode
#value = urllib.parse.urlencode(id)
#print(value)


value = urllib.parse.quote(twoWorlds)
print(value)

value = urllib.parse.quote("two worlds")
print(value)