import requests
import elementtree as ET
from dict2xml import dict2xml

class Action(object):
    _actionTemplate = '''<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">
       <SourcedFixletAction>
               <SourceFixlet>
                       <Sitename>ActionSite</Sitename>
                       <FixletID>%%FixletID</FixletID>
                       <Action>Action1</Action>
               </SourceFixlet>
               <Target>
                       <ComputerName>%%TargetName</ComputerName>
               </Target>
               <Parameter Name="%%ParameterName"></Parameter>
       </SourcedFixletAction>
</BES>'''
   def __init__(self):
      pass

   @property
   def actionTemplate(self):
       """ get the template """
       return self._actionTemplate

   def actionFactory(fixletID, targetName, parameterName=pName, parameterValue=pvalue):
      return _actionTemplate

action = { 'SourceFixletAction': {
      'SourceFixlet': {
         'Sitename' : 'ActionSite',
         'FixletID' : '',
         'Action'   : 'Action1'
         },
      'Target' : {
         'ComputerName' : ''
         }
      }
    }

baseurl = 'https://localhost:52311/api/'
files = {'file': open('stopBesGather.xml', 'rb')}

r = requests.get('https://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

# issue action specified in stopBesGather.xml
r = requests.post(baseurl+'actions',verify=False,auth=('adminMO','adminmo'), data=open('stopBesGather.xml', 'rb'))

if r.status_code != 200:
   print r.status_code


print '\nHeres the XML about the action that I got back: \n', r.text



