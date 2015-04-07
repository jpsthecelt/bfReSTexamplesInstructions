import requests
import xml.etree.ElementTree as ET

baseurl = 'http://localhost:52311/api/'

r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code
#else:
#   print('too bad sucka: %s')
myRequest = baseurl+'query?relevance=(name of fixlet of it) of results from (bes fixlets whose (display name of site of it contains "Patches for Windows (English)" and fixlet flag of it = true)) whose (exists last became relevant of it and relevant flag of it = false) of bes computers whose (name of it contains "GRASS")'

r = requests.get(myRequest,verify=False,auth=('adminMO','adminmo'))

#r = requests.get('http://localhost:52311/api/fixlets/master',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code
#else:
#   print('GRASSKEET: %s', r.text)
file = open('./fixedFixlets.txt', 'w')
file.write(r.text)
file.close()
#root = ET.fromstring(r.text)
##for child in root:
##   print child.tag, child.attrib
#i = []
#n = []
#for fixlet in root.findall('Answer'):
#   n.append(fixlet.find('Result').text)
#   i.append(fixlet.find('Evaluation').text)
#   print fixlet.text
##   n.append(fixlet.find('Name').text)
##   i.append(fixlet.find('ID').text)
#d = dict(zip(i,n))
#
#for key in iter(d):
#   print key,d[key]
#for name in root.iter('Name'):
#   print name.attrib

#r = requests.get('http://localhost:52311/api/fixlet/master/7217',verify=False,auth=('adminMO','adminmo'))
#if r.status_code == 200:
#   print(r.text)
#else:
#   print('too bad sucka: %s')
#
#files = {'file': open('stopBesGather.xml', 'rb')}
#url = 'http://localhost:52311/api/actions'
#r = requests.post(url, verify=False,auth=('adminMO','adminmo'), files=files)
#print( r.text )
#



