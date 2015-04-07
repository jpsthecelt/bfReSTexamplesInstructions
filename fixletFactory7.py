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
            }
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
# Initialize super-class, grab the prototype XML, edit, and stuff into _myActionXML
        super(Action,self).__init__()
        xml = super(Action,self).actionTemplate
        self._myActionXmlTree = ET.fromstring(xml) # now we should do something with the tree, & edit it, here
        self_myActionXML = formatFixlet( xml, fixletID, targetName, parameterName, parameterValue )
    @property
    def myActionXML(self):     # accessor for resultant XML
        """ get the template """
        return self._myActionXML
    @myActionXML.setter
    def actionTemplate(self, xml):
        self._myActionXML = xml
    def formatFixlet(xmlTemplate, fID, tName, pName, pValue ):
        if len(fID) > 0:
            newXml = xmlTemplate.replace('%%FixletID', fID, 1)
        if len(tName) > 0:
            newXml = xmlTemplate.replace('%%TargetName', tName, 1)
        if not pName is None:
            newXml = xmlTemplate.replace('%%ParameterName', pName, 1)
        if not pValue is None:
            newXml = xmlTemplate.replace('%%ParameterValue', pValue, 1)
        if pName is None or pValue is None:
            newXml = xmlTemplate.replace('                   <Parameter Name="%%ParameterName">%%ParameterValue</Parameter>\n', '', 1)
        return newXml

if __name__ == '__main__':
#
# So, create the XML for a new action, calling CTOR with the appropriate parameters   
#    
    c = Action('121', 'GRASSKEET')
    print "\nThe initialized OrderedDictionary XML from actionDict is: ", c.actionTemplate

    print "\nHere's the modified XML from the custom initializer: \n", c.myActionXML

    d = Action('121', 'GRASSKEET', parameterName='Parm1', parameterValue='Parm2')
    print "\nHere's the second of two modified XMLs (with Parameters): \n", d.myActionXML

