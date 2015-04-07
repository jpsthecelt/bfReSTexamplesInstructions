import json
import collections
from dicttoxml import dicttoxml

class PrototypeAction(object):
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
    def actionTemplate(self):
        self._actionDict = dicttoxml(self.getJson(), root=False, attr_type=False)
        return self._actionDict


# Previous contents of 'fixletFactory4.py
#--------------------------------------------
#
# The following class, Action, is a subclass of PrototypeAction, & has a 4-item initializer.
#
# If it is called with no parameterName or parameterValue arguments, the returned
# string is editted to remove the <Parameter.... Parameter> line from the XML.
#
# Both classes use the @property statement to define accessor functions
#
class Action(PrototypeAction):
    """ Using parameters supplied to __init__(), edit prototype into new XML for fixlet; providing accessor function """
    def __init__(self, fixletID, targetName, parameterName=None, parameterValue=None):
        super(Action,self).__init__()
        self._myActionXML = super(Action,self).actionTemplate           # Grab the prototype XML and stuff into _myActionXML, then edit
        if len(fixletID) > 0:
            self._myActionXML = self._myActionXML.replace('%%FixletID', fixletID, 1)
        if len(targetName) > 0:
            self._myActionXML = self._myActionXML.replace('%%TargetName', targetName, 1)
        if not parameterName is None:
            self._myActionXML = self._myActionXML.replace('%%ParameterName', parameterName, 1)
        if not parameterValue is None:
            self._myActionXML = self._myActionXML.replace('%%ParameterValue', parameterValue, 1)
        if parameterName is None or parameterValue is None:
            self._myActionXML = self._myActionXML.replace('                   <Parameter Name="%%ParameterName">%%ParameterValue</Parameter>\n', '', 1)
    @property
    def myActionXML(self):     # accessor for resultant XML
        """ get the template """
        return self._myActionXML
    @myActionXML.setter
    def actionTemplate(self, xml):
        self._myActionXML = xml

if __name__ == '__main__':
#
# So, create the XML for a new action, calling CTOR with the appropriate parameters   
#    
    c = Action('121', 'GRASSKEET')
    print "\nThe initialized OrderedDictionary XML from actionDict is: ", c.actionTemplate

    print "\nHere's the modified XML from the custom initializer: \n", c.myActionXML

    d = Action('121', 'GRASSKEET', parameterName='Parm1', parameterValue='Parm2')
    print "\nHere's the second of two modified XMLs (with Parameters): \n", d.myActionXML

