import requests

baseurl = 'https://localhost:52311/api/'
files = {'file': open('testPostParameter.xml', 'rb')}

r = requests.get('https://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

# issue action specified in stopBesGather.xml
r = requests.post(baseurl+'actions',verify=False,auth=('adminMO','adminmo'), data=open('testPostParameter.xml', 'rb'))

if r.status_code != 200:
   print r.status_code


print '\nHeres the XML about the action that I got back: \n', r.text



