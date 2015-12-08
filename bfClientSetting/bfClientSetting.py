# AUTHOR: Created by John Singer, 4.13.15-7.21.15
# Any usage must include giving credit to the above author,
# but there is no warranty, express or implied for the use of this code.
#
#  If problems are encountered, your 'best bet' is to ask for help
# on the bigfix forum (http://forum.bigfix.com). I.E. this is 'unsupported'
# code.
#

import sys
import json
import xml.etree.ElementTree as ET
import requests
import argparse

requests.packages.urllib3.disable_warnings()
usage = """bfClientSetting.py <computername> -c <parameter> [options]

where <computername> is the name of the target computer on which we should
get/change/create the indicated ClientSetting.  This corresponds to the 
individual client-settings we can set with the BF Console 'right-click'
on the individual computers.

Options:
So far, this program only responds to the following parameters, each of 
which can have the values of either 0 or 1, or can be queried by supplying
no value:
CF_SystemType 
CF_Property1
CF_Property2

  -v <value>   
  -s <servername>       name of the system hosting the BigFix server
  --user USERNAME             IEM console-login USERNAME
                               (no default)
  --password PASSWORD         IEM console-login PASSWORD for above user
                               (no default)
  -h, --help                   Print this help message and exit

Examples:
    python bfClientSetting.py GRASSKEET -c CF_SystemType -v 1 -s GRASSKEET adminMO adminmo
Which sets the value of the client-setting CF_SystemType on system GRASSKEET adminMO adminmo

    python bfClientSetting.py GRASSKEET -s CF_SystemType -s GRASSKEET
    would get the value of CF_SystemType on system GRASSKEET
"""


# When invoked as the main program, take the command-line parameters & query/set the indicated
#      ClientSettings
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='get/set a clientsetting on indicated computer')
# positional parameters
        parser.add_argument('computername',  type=str, help='The target computer on which to examine/set client settings' )
        parser.add_argument('username',  type=str, help='A valid BF username')
        parser.add_argument('password',  type=str, help='A valid BF password')
        parser.add_argument('-c',  default="CF_SystemType", choices=['CF_SystemType', 'CF_Property1', 'CF_Property2'], help="settings to set")
        parser.add_argument('-v', type=str, help='the value' )
        parser.add_argument('-s',  type=str, help='Name of the BF server')

        if '-h' in sys.argv or '--help' in sys.argv:
            print(usage)
            exit()

        args = parser.parse_args()

        if args.computername == None or args.c == None or args.username == None or args.password == None or args.s == None:
           exit(status=1)
        else:
           if args.c: settingName = args.c
           if args.v != None:
               tgtSetting = args.v
           else:
               tgtSetting = ""

        if args.username: user = args.username
        if args.password: password = args.password

        if args.s:
            sn = args.s
        else:
            sn = 'localhost'

        if args.computername:
            tgtMachine = args.computername
        else:
            tgtMachine = 'grasskeet'

#        print("~ computername: {}".format(args.computername))
#        print("~ username: {}".format(args.username))
#        print("~ password: {}".format(args.password))
#        print("~ settingName: {}".format(args.c))
#        print("~ setting: {}".format(args.v))

# Now, login to the BF server
        bfUrlBase  = 'https://'+sn+':52311/api'
        bfUrlLogin = 'http://'+sn+':52311/api/login'

        r = requests.get(bfUrlLogin,verify=False,auth=(user,password))
        if r.status_code != 200:
           print ('login error: ', r.status_code)
           exit(status=2)

        computerIDrq = bfUrlBase+'/query?relevance=(name of it,id of it) of bes computers whose (name of it contains "%TARGET%")'.replace('%TARGET%', tgtMachine)

        r = requests.get(computerIDrq,verify=False,auth=(user,password))
        if r.status_code != 200 or not ('Answer' in r.text):
            print ('ComputerID query for {} Error: {}'.format(tgtMachine, r.status_code))
            exit(status=3)

# Extract the first computer ID to be used in the next query/post
        root = ET.fromstring(r.text)
        cName = root.findall('Query/Result/Tuple/Answer')

# Look for ID matching commandline computer-name (Case is significant)
        cID=""
        for i in range(len(cName)):
          if cName[i].text == tgtMachine:
             cID = cName[i+1].text
             break;

# Ensure that we found the proper computer ID/Name
        if len(cID) <= 0:
            print('\nRequested Computer Not Found: {}'.format(tgtMachine))
            exit(4)

# Get or post, depending on commandline parameters
        if len(tgtSetting) <= 0:
            r = requests.get(bfUrlBase+'/computer/'+cID+'/setting/'+settingName, verify=False, auth=(user, password))
        else:
            settingProto = ET.ElementTree(file='./settingProto.xml')
#            root = settingProto.getroot()
            newSettings = ET.tostring(settingProto.getroot())

            r = requests.get(bfUrlLogin,verify=False,auth=(user,password))
            newSettings = newSettings.replace('%%tgt_computer', tgtMachine)
            newSettings = newSettings.replace('%%setting_name', settingName)
            newSettings = newSettings.replace('%%setting_value', tgtSetting)
            newSettings = newSettings.replace('%%computer_id', cID)

            postUrl = "{0}/computer/{1}/settings".format(bfUrlBase, cID)
            value = ""
            r = requests.post(postUrl, data=newSettings, verify=False, auth=(user, password))

        if r.status_code != 200:
            print('bfClientSetting ERROR -- Status: ', r.status_code, 'Headers:', r.headers)
            exit()
        else:
            if 'Value' in r.text:
                xans = ET.fromstring(r.text)
                value = xans.find('ComputerSettings/Setting/Value').text
            else:
                if not '<ID>' in r.text:
                    print('\nNo setting {} in {}'.format(settingName,tgtMachine))
                    exit()
                else:
                    value = tgtSetting

            if len(value) > 0 or '<ID>' in r.text:
                print('\nValue of {} is {}'.format(settingName,value))
            else:
                print('\nSetting {} not found'.format(settingName))

# Handle any exceptions, printing out error code
    except SystemExit:
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        print("\n")
