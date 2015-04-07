import xml.etree.ElementTree as ET
from dict2xml import dict2xml
from collections import OrderedDict
import json
import sys

xmlRoot = '<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">'
class PrototypeAction(object):
    def __init__(self):
        self._actionTemplate = '''<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">
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

    @property
    def actionTemplate(self):
        """ get the template """
        return self._actionTemplate

class Action(PrototypeAction):
    def __init__(self):
        super(Action,self).__init__()
        self._myActionXML = super(Action,self).actionTemplate

#    @property
    def myActionXML(self):
        """ get the template """
        return self._myActionXML

if __name__ == '__main__':
    p = PrototypeAction()
    print "Prototype XML is", p.actionTemplate
    b = Action()
    print "Here's the original XML", b.actionTemplate
    print "Here's the modified XML", b.myActionXML
#        a = Action()
#        print "Here's the initial XML", a.actionTemplate
#except:
#    print "Error in program: ", sys.exc_type, sys.exc_value
#     def __init__(self, fixletID=None, targetName=None, parameterName=None, parameterValue=None):
#        if fixletID != None:
#            self._myActionXML = self._myActionXML.replace('%%FixletID', fixletID, 1)
#            self.fixletID = fixletID
#        if targetName != None:
#            self._myActionXML_myActionXML = self._myActionXML.replace('%%TargetName', targetName, 1)
#            self.targetName = targetName
#        if parameterName != None:
#            self._myActionXML_myActionXML = self._myActionXML.replace('%%ParameterName', parameterName, 1)
#            self.parameterName = parameterName
#        if parameterValue != None:
#            self._myActionXML_myActionXML= self._myActionXML.replace('%%FixletID', parameterValue, 1)
#            self.paramaterValue = parameterValue
#        if parameterName == None or parameterValue == None:
#            self._myActionXML_myActionXML = self._myActionXML.replace('<Parameter Name="%%ParameterName">%%ParameterValue</Parameter>', None, 1)
#
