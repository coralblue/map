import httplib2
import json

import urllib.request as ur
import urllib.parse as par

from tornado import escape


def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyC58ELvX4szZRChd3tnNPVeg7DFaoSAibY"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, google_api_key))
    # html = ur.urlopen(url).read()
    # data = json.loads(html.decode('utf-8'))
    # print (data)
    html = ur.urlopen(url).read()
    h = json.loads(html.decode('utf-8')) 
    # h = httplib2.Http()
    # html = httplib2.Http()
    # h = json.loads(html.decode('utf-8'))
    # h = escape.json_decode(html)
    # resoponse, content = h.request(str(url), 'GET')
    resoponse, content = h.request(url, 'GET')
    # # c = escape.json_decode(content)
    content = str(content)
    result = json.loads(content)
    # # result = json.loads(c)
    return result

    # print ("response header: %s \n \n" % response)
