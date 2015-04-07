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

# Now POST the fixlet to the master action site (.../fixlets/master)
#    it'll 'show up' in the console, under 'my custom content'
r = requests.post(baseurl+'fixlets/master',verify=False,auth=('adminMO','adminmo'), data=open('TweedleDee.bes','rb'))

if r.status_code != 200:
   print r.status_code

print 'Heres the XML I got back from POSTing', r.text

