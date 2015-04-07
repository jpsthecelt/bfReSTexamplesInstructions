# We are using the 'requests' library as it makes simple username/password authentication easy (for this example, only)
# we also use the ElementTree library to simplify XML parsing/manipulation
import requests
import xml.etree.ElementTree as ET

# log in.
r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

baseurl = 'https://localhost:52311/api/'
r = requests.get(baseurl+'fixlets/external/BES Support',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

# point to the 'root' of the tree of XML data, then build a dictionary by filling two different arrays, then
#       'zipping' (combining) together...
root = ET.fromstring(r.text)
#for child in root:
#   print child.tag, child.attrib
i = []
n = []

print 'starting search in results'
for fixlet in root.findall('Fixlet'):
   n.append(fixlet.find('Name').text)
   i.append(fixlet.find('ID').text)

print 'creating dictionary'
d = dict(zip(i,n))

# display the results as list in  ID#, name format
print 'try to print dict'
for key in iter(d):
   print key,d[key]



