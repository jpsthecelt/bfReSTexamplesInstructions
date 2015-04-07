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
    print "Here's the modified XML from the custom initializer: \n", c.myActionXML

    d = Action('121', 'GRASSKEET', parameterName='Parm1', parameterValue='Parm2')
    print "\nHere's the second of two modified XMLs (with Parameters): \n", d.myActionXML
