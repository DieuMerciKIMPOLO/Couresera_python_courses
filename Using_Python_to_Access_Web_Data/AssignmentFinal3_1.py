import urllib.request, urllib.parse, urllib.error
import json
url = input('Enter location: ')
uh = urllib.request.urlopen(url)
som=0
data = uh.read()
fichier=json.loads(data)
comments=fichier['comments']
for com in comments:
	som+=int(com['count'])
print(som)
#print(tree.findall('comments/comment'))
#http://py4e-data.dr-chuck.net/comments_57354.xml
#http://py4e-data.dr-chuck.net/comments_42.xml
