import json
import collections
from dicttoxml import dicttoxml

class PrototypeActionDict:
    def __init__(self):
        self._j = '''{
    "BES": {
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
    }
}'''
    def getJson(self):
        return json.loads(self._j, object_pairs_hook=collections.OrderedDict)
    @property
    def actionDict(self):
        self._actionDict = dicttoxml(self.getJson(), root=False, attr_type=False)
        return self._actionDict

if __name__ == '__main__':
    p = PrototypeActionDict()
    print "\nThe initialized OrderedDictionary XML from actionDict is: ", p.actionDict


#        return self._j

#    "Parameter Name="%%ParameterName"": "%%ParameterValue"
#   self._actionDict = dict(self._j)
#   self._actionDict = dict(self._j)
#    x = dicttoxml(p.getJson(), root=False, attr_type=False)
#    print "\nThe initialized XML (from OrderedDictionary) is: ", x
