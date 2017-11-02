
import json

query = {}

term = {}
term["$term"] = "foo jc"

search = {}
search["$search"] = term

text = {}
text["$text"] = search

query["name"] = text


result = json.dumps(query)

print(result)