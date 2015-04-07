import requests
import xml.etree.ElementTree as ET

baseurl = 'http://localhost:52311/api/'

r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code
#else:
#   print('too bad sucka: %s')
myRequest = baseurl+'query?relevance='(name of it,operating system of it&"@"&value of results from (bes properties whose (name of it contains "Last Report Time")) of it) of members of bes computer group whose (name of it as lowercase contains "win")'

r = requests.get(myRequest,verify=False,auth=('adminMO','adminmo'))

if r.status_code != 200:
   print r.status_code

#file = open('c:/AssetsWCheckinTime.txt', 'w')
#file.write(r.text)
#file.close()
root = ET.fromstring(r.text)
#for child in root[0][0][0]:
#   print child.tag, child.attrib
i = []
n = []

print 'starting search in results'
for ans in root.findall('Result'):
    print ans.find('Answer').text
#   n.append(ans.find('Answer').text)


print 'creating dictionary'
#d = dict(zip(i,n))
d = dict(n)

# display the results as list in  ID#, name format
print 'try to print dict'
#for key in iter(d):
#   print key,d[key]
for q in iter(d):
    print q
    file.write(n)

file.close
