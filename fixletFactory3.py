# !/usr/bin/python

import sys

class PrototypeAction(object):
    """ The PrototypeAction class simply holds the prototypical XML for an action & provides an accessor for it. """
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
    def actionTemplate(self):        # Accessor for prototype XML
        """ get the template """
        return self._actionTemplate

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
    def __init__(self, fixletID=None, targetName=None, parameterName=None, parameterValue=None):
        super(Action,self).__init__()
        self._myActionXML = super(Action,self).actionTemplate           # Grab the prototype XML and stuff into _myActionXML, then edit
        if fixletID != None:
            self._myActionXML = self._myActionXML.replace('%%FixletID', fixletID, 1)
        if targetName != None:
            self._myActionXML = self._myActionXML.replace('%%TargetName', targetName, 1)
        if parameterName != None:
            self._myActionXML = self._myActionXML.replace('%%ParameterName', parameterName, 1)
        if parameterValue != None:
            self._myActionXML = self._myActionXML.replace('%%FixletID', parameterValue, 1)
        if parameterName == None or parameterValue == None:
            self._myActionXML = self._myActionXML.replace('                   <Parameter Name="%%ParameterName">%%ParameterValue</Parameter>\n', '', 1)
    @property
    def myActionXML(self):     # accessor for resultant XML
        """ get the template """
        return self._myActionXML

if __name__ == '__main__':
#
# So, create the XML for a new action, calling CTOR with the appropriate parameters   
#    
    c = Action(fixletID='121', targetName='GRASSKEET', parameterName=None, parameterValue=None)
#    print "Here's the original XML from actionTemplate: ", c.actionTemplate
    print "Here's the modified XML from the custom initializer: \n", c.myActionXML
