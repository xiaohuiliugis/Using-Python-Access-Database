# this is the assigment for Using Python to Access Web Data, Week 5
# on XML


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)

    url = urllib.request.urlopen(address,context =ctx)
    xml_data = url.read()
    
    print('Retrieved', len(xml_data), 'characters')
    print (url)
    print (xml_data)
    #print(xml_data.decode())

    # ET.fromstring()converts xml structured string to tree format
    tree = ET.fromstring(xml_data)

    lst = tree.findall('comments/comment')
    print ("user count:", len(lst))
    total = 0
    for item in lst:
        total += int(item.find('count').text)
    print (total)
    #print (results)
    #lat = results.find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    # print('lat', lat, 'lng', lng)
    # print(location)
