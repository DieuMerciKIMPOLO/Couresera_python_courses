# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Ryhs.html'
for x in range(1,8):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	print(tags[17].contents[0])
	url=tags[17].get('href', None)
#for tag in tags:
    # Look at the parts of a tag
    #som+=int(tag.contents[0])
#print(som)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)