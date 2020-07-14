# this is the assigment for Using Python to Access Web Data, Week 6
# on JSON
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = urllib.request.urlopen(address,context =ctx).read()
    #print('Retrieving', url)
    
    data = url.decode()
    print('Retrieved', len(data), 'characters')
    #print(data)

    try:
        js = json.loads(data)
    except:
        js = None

    total = 0
    for item in js['comments']:
        #print   (item['count'])
        total += item['count']
    print (total)


