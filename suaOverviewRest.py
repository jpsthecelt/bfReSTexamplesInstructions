import json
import requests
#
# Author: John Singer, Channels BigFix CTP
# Purpose: As an educational-resource for both customers and CTPs, to learn
#          how to extract SUA report information via ReST.
#          This grabs and displays the SUA 'software_instances' information
#          for all systems. For more information on this, see:
#              http://www-01.ibm.com/support/knowledgecenter/SSKLLW_9.1.0/com.ibm.tivoli.tem.doc_9.1/SUA_9.1/com.ibm.license.mgmt.doc/integration/t_license_use_selected.html?lang=en

# Note that for this exercise, you must login into the SUA web report Console, go to 
#      the Account/preferences/Show token screen of SCA, to grab the SSL 
#      token and save it to a file as indicated, below. Your file should read
#      something like the following (no spaces, no quotes).
#
#      token=137806544748ddbf083d7849cbfecf8a7fb41bc2
#
# $Id$:
#
if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
       print "\n**** Usage: python suaOverviewRest.py <tokenFile.txt>\n"
       exit()
    else:
        iptLine = open(sys.argv[1]).read().split('\n')

# So, we've pulled the filename off the commandline, opened it, removed the newline
#     and now we'll assign the variable 'token' to the right half after the '=' 
    token = iptLine[0].split('=')[1]

# Now that the token is set, let's decide on what we want to request, build the URL and do a GET
overviewInfo = 'https://9.39.122.183:9081/api/sam/'
computers = 'computer_systems'
lu = 'license_usages'
si = 'software_instances'
ul = '&limit=100'
sf = 'software_facts'
oi = overviewInfo + computers
ovUrl = oi + '?token=' + token + ul
#+ '&limit=100000&offset=100000'

r = requests.get(ovUrl,verify=False)

# check to see if the server responded appropriately
if r.status_code != 200:
   print r.status_code
   exit()
else:
    data = json.loads(r.text)

# Find the computer-name/ID mapping & fill a table:
computerList = {}
for c in data['rows']: 
    if c['host_name'] is not None:
        cId = c['id']
        computerList[cId] = c['host_name']
#        print "\nHostname:", c['host_name'], ", Id: ", c['id']

# Now, using the computer-name/ID mapping, let's query for some 'software instances'; i.e. computer-name and software-titles installed on that machine
oi = overviewInfo + si
ovUrl = oi + '?token=' + token + '&columns[]=computer_system_id&columns[]=catalog_dimension.software_title_name' + ul

r = requests.get(ovUrl,verify=False)

# check to see if the server responded appropriately
if r.status_code != 200:
   print r.status_code
   exit()
else:
    data = json.loads(r.text)

print "\nSoftware Installed: "

# print out the computer and installed software
for c in data['rows']: 
    if c['computer_system_id'] is not None:
        print "\n", computerList[c['computer_system_id']], ": ", c['catalog_dimension']['software_title_name']
   
