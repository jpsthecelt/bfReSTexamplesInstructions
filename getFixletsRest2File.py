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

if r.status_code != 200:
   print r.status_code

file = open('c:/fixedFixlets.txt', 'w')
file.write(r.text)
file.close()
