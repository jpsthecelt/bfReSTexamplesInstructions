#!/usr/bin/env python

from argparse import ArgumentParser
import hashlib
import os
import sys
import urllib2
from urlparse import urlparse
import requests
import xml.etree.ElementTree as eT

usage = """createComputerGroup.py <group filename> <group name> [options]

Create a group within IBM Endpoint Manager master-actionsite for use in
       targetting fixlets

The first parameter, the desired name of the group-to-be-created
    must not currently exist within IEM

The second parameter, the name of a text file containing a
    one-computername-per-line list of IEM-managed computers to include

Options:
  -u USERNAME                 IEM console-login USERNAME
                               (no default)
  -p PASSWORD                 IEM console-login PASSWORD for above user
                               (no default)
  -h, --help                   Print this help message and exit

Examples:
  Create a group named USAA-PatchTuesday-2

    createComputerGroup USAA-PatchTuesday-2 fromFile.txt -u adminMO -p adminmo

"""

def appendMemberComputer(element, xmlNode):
    '''Inserts the xmlNode as a condition for group membership.'''
    element.append(eT.fromstring(xmlNode))
    return element

if __name__ == '__main__':
    baseurl = 'https://localhost:52311/api/'
    stanza = '<SearchComponentPropertyReference PropertyName="Computer Name" Comparison="Contains"><SearchText>%%computer</SearchText><Relevance>exists (computer name) whose (it as string as lowercase contains "%%computer" as lowercase)</Relevance></SearchComponentPropertyReference>'

    tree = eT.ElementTree(file='./protoComputerGroup.xml')
    root = tree.getroot()
    lines = [line.rstrip('\n\r').lower() for line in open('target_computer_group.txt', 'rb')]
    insertPoint = eT.Element('JoinByInterSection')
    for computerName in lines:
        el = appendMemberComputer(insertPoint, stanza.replace('%%computer', computerName, 2))

    newXml = eT.tostring(el)
    print "\nreturned XML is: ", newXml
    root = tree.getroot()
    print "\nSubstituted XML is: ",eT.tostring(insertPoint)
    exit()

    r = requests.get('https://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
    if r.status_code != 200:
       print r.status_code
    
    # issue action specified in stopBesGather.xml
    r = requests.post(baseurl+'computergroups/master/actionsite',verify=False,auth=('adminMO','adminmo'), data=eT.tostring(newXml))
    
    if r.status_code != 200:
       print r.status_code
    
    
    print '\nHeres the XML about the action that I got back: \n', r.text

# 



