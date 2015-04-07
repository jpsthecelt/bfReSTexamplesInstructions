import json
import collections
from dicttoxml import dicttoxml

class PrototypeActionDict:
    def __init__(self):
        self._xml = '''<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">
     <SourcedFixletAction>
          <SourceFixlet>
                  <Sitename>ActionSite</Sitename>
                  <FixletID>%%FixletID</FixletID>
                  <Action>Action1</Action>
          </SourceFixlet>
          <Target>
                  <ComputerName>%%TargetName</ComputerName>
          </Target>
          <Parameter Name="%%ParameterName">%%ParameterValue</Parameter>
     </SourcedFixletAction>
</BES>'''
        self._j = '''{
    "SourceFixletAction": {
     "SourceFixlet": {
        "Sitename": "ActionSite",
        "FixletID": "%%FixletID",
        "Action": "Action1"
        },
    "Target": {
        "ComputerName": "%%TargetName" 
        },
    "Parameter Name": "Parameter Value"
    }
}'''
    def getXml(self):
        return self._xml
    def getJson(self):
        return self._j

#    "Parameter Name="%%ParameterName"": "%%ParameterValue"
#        self._actionDict = dict(self._j)
#   @property
#   def actionDict(self):
#       return self._actionDict
#
if __name__ == '__main__':
    p = PrototypeActionDict()

    j = p.getJson()
    d = json.loads(j, object_pairs_hook=collections.OrderedDict)
#    x = dicttoxml(d, custom_root='BES')
    x = dicttoxml(d, root=False)
    print "\nthe resultant XML is: ", x
#    d = json.loads(p.getJson(), object_pairs_hook=collections.OrderedDict)
#    print "XML is: ", d.getXML(), "\nJSON is: ", j
#    print "Dict2XML is: ", dict2xml(d)
