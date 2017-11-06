 

#Python 3. The urllib.urlencode() function is now urllib.parse.urlencode(), 
# and the urllib.urlopen() function is now urllib.request.urlopen().

import http.client , urllib


params = urllib.parse.urlencode({"where":{"spotify":{"$exists":"true"}}})
 
 
print(params)


