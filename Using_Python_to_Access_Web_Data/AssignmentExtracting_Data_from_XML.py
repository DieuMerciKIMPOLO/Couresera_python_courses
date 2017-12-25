import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
som=0
for val in tree.findall('comments/comment'):
	som+=int(val.find('count').text)
print(som)
#print(tree.findall('comments/comment'))
