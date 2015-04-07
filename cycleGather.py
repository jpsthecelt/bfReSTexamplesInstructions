import requests
import xml.etree.ElementTree as ET

start = '637'
stop = '636'
target = 'GRASSKEET'

x = ET.parse('./cycleGather.xml')
r = x.getroot()     # get the root of the elementTree
url = 'https://GRASSKEET:52311/api/actions'
r[0][0][1].text = start # stop Bes Gather
r[0][1][0].text = target

print 'post example>>'
#r = requests.post(url, verify=False,auth=('adminMO','adminmo'), files=ET.dump(x))
r = requests.post(url, verify=False,auth=('adminMO','adminmo'), files='./startBesGather.xml')
if r.status_code != 200:
    print( r.text )
else:
    print ('Status Code : '+str(r.status_code))
