# /usr/bin/python
import urllib3
import xml.etree.ElementTree as ET
 
baseurl = 'http://grasskeet:52311/api'
 
http = urllib3.PoolManager()
url = baseurl + '/login'
headers = urllib3.util.make_headers(basic_auth='adminMO:adminmo')
urllib3.disable_warnings()
 
r = http.request('GET', url, headers=headers)
 
if r.status != 200:
   print r.status
 
url = baseurl+'/fixlets/external/BES%20Support'
headers = urllib3.util.make_headers(basic_auth='adminMO:adminmo')
urllib3.disable_warnings()
 
r = http.request('GET', url, headers=headers)
 
if r.status != 200:
   print r.status
 
if r.status != 200:
   print r.status
 
root = ET.fromstring(r.data)
 
i = []
n = []
print 'starting search in results'
for fixlet in root.findall('Fixlet'):
   n.append(fixlet.find('Name').text)
   i.append(fixlet.find('ID').text)
print 'creating dictionary'
d = dict(zip(i,n))
 
print 'try to print dict'
for key in iter(d):
   print key,d[key]
