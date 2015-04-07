# With this script, we're going to take an exported fixlet, 'TweedleDee.bes'
#    and import it into the console using the ReST API.


# notice that this uses the Python Egg called Requests; 
#    it simplifies REST authentication, such that I can easily specify the URL,
#    the fact that I'm bypassing any SSL Cert, and my username/password.
import requests
import xml.etree.ElementTree as ET

baseurl = 'https://localhost:52311/api/'

# open saved fixlet XML file
files = {'file': open('TweedleDee.bes', 'rb')}

# Login to REST Api...
r = requests.get('https://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

r = requests.post(baseurl+'fixlets/master',verify=False,auth=('adminMO','adminmo'), data=open('TweedleDee.bes','rb'))

#r = requests.get('http://localhost:52311/api/fixlets/master',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code
#else:
#   print('too bad sucka: %s')
print 'Heres the XML', r.text
#root = ET.fromstring(r.text)
#for child in root:
#   print child.tag, child.attrib
#i = []
#n = []
#print 'starting search in results'
#for fixlet in root.findall('Fixlet'):
#   n.append(fixlet.find('Name').text)
#   i.append(fixlet.find('ID').text)
#print 'creating dictionary'
#d = dict(zip(i,n))
#
#print 'try to print dict'
#for key in iter(d):
#   print key,d[key]
#for name in root.iter('Name'):
#   print name.attrib
#
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



