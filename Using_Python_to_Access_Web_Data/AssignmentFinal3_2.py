
import urllib.request, urllib.parse, urllib.error
import json
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})
uh = urllib.request.urlopen(url)
data = uh.read().decode()
fichier=json.loads(data)
print(fichier['results'][0]['place_id'])