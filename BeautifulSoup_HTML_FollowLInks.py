# This is the assignment for Using Python to Acess Web Data_Week 4
# Using BeautifulSoup to acces Html 
# To run this, you can install BeautifulSoup
# I installed BeautifulSoup using: pip install Beautifulsoup 4

# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
link_pos = int(input('Enter position -'))
count = int(input('Enter count -'))


# Retrieve all of the anchor tags
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
# this following code is extremely smart!
while count >=0:
	html = urllib.request.urlopen(url,context =ctx).read()
	soup = BeautifulSoup(html,"html.parser")
	
	tags = soup('a')
	print (url)
	print ("Name:",tags[link_pos-1].contents[0])

    # this statement change the url to be the newest one found in one html page
	url = tags[link_pos-1].get("href",None)
	
	count -=1
