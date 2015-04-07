import requests
import xml.etree.ElementTree as ET

#start = '7233'
#stop = '7234'
start = '637'
stop = '636'

target = 'GRASSKEET'

x = ET.parse('./cycleGather.xml')
r = x.getroot()     # get the root of the elementTree
url = 'https://localhost:52311/api/actions'
#r[0][0][1].text = '7233' # stop Bes Gathe
r[0][1][0].text = target
r[0][0][1].text = '636' # stop Bes Gather

print 'post example>>'
#r = requests.post(url, verify=False,auth=('adminMO','adminmo'), files=ET.dump(x))
r = requests.post(url, verify=False,auth=('adminMO','adminmo'), files='./stopBesGather.xml')
if r.status_code != 200:
    print( r.text )
else:
    print ('Status Code : '+str(r.status_code))
