import requests
import xml.etree.ElementTree as ET

baseurl = 'http://localhost:52311/api/'

r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code


baseurl = 'https://localhost:52311/api/'

r = requests.get(baseurl+'fixlets/external/BES Support',verify=False,auth=('adminMO','adminmo'))

if r.status_code != 200:
   print r.status_code

root = ET.fromstring(r.text)

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
