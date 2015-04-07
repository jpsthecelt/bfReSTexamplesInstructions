import requests
import xml.etree.ElementTree as ET

#prototype = 
#"""<?xml version="1.0" encoding="UTF-8"?>
#<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">
#<SourcedFixletAction>
#<SourceFixlet>
#<Sitename>TestSite</Sitename>
#<FixletID>83</FixletID>
#<Action>Action1</Action>
#</SourceFixlet>
#<Target>
#<ComputerName>bhobbs-db</ComputerName>
#</Target>
#<Parameter Name="_BESClient_EMsg_Detail">1000</Parameter>
#</SourcedFixletAction>
#</BES>"""
#
#prelude = """
#<?xml version="1.0" encoding="UTF-8"?>
#<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">
#    <SingleAction>
#        <Title><![CDATA[Stop two Services]]></Title>
#        <Relevance><![CDATA[false]]></Relevance>
#        <ActionScript MIMEType="application/x-sh"><![CDATA["""
#
#postlude = """
#>]]></ActionScript>
#        <SuccessCriteria Option="RunToCompletion"/>
#        <Target>
#            <ComputerName>1</ComputerName>
#        </Target>
#    </SingleAction>
#</BES>"""
#
baseurl = 'http://localhost:52311/api/'

r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code
#else:
#   print('too bad sucka: %s')
baseurl = 'https://localhost:52311/api/'
#r = requests.get(baseurl+'fixlets/master',verify=False,auth=('adminMO','adminmo'))
r = requests.get(baseurl+'fixlets/external/BES Support',verify=False,auth=('adminMO','adminmo'))

#r = requests.get('http://localhost:52311/api/fixlets/master',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code
#else:
#   print('too bad sucka: %s')

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

print 'try to print dict'
for key in iter(d):
   print key,d[key]
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



