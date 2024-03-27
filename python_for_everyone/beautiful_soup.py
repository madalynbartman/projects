import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Beautiful soup parses html. You can feed it the worst html ever
# and it will use it's incredible brain to parse it.
# Return list of anchor tags, etc.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
