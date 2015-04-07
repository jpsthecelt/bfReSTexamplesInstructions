import json
import requests
#
# Author: John Singer, Channels BigFix CTP
# Purpose: As an educational-resource for both customers and CTPs, to learn
#          how to extract SCA report information via ReST.
#          This grabs and displays the SCA Overview page information
#          in a slightly different format.
# Note that for this exercise, you must login into the SCA reports, go to 
#      the Account/preferences/Show token screen of SCA, to grab the SSL 
#      token and save it to a file as indicated, below. the file should read
#      something like the following (no spaces, no quotes).
#
#      token=137806544748ddbf083d7849cbfecf8a7fb41bc2
#
# $Id$:
#
#token=137806544748ddbf083d7849cbfecf8a7fb41bc2
if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
       print "\n**** Usage: python scaOverviewRest.py <tokenFile.txt>\n"
       exit()
    else:
        iptLine = open(sys.argv[1]).read().split('\n')

# So, we've pulled the filename off the commandline, opened it, removed the newline
#     and now we'll assign the variable 'token' to the right half after the '=' 
    token = iptLine[0].split('=')[1]


overviewInfo = 'http://tomato/api/scm/overview'
ovUrl = overviewInfo + '.json?token=' + token

r = requests.get(ovUrl)

# check to see if the server responded appropriately
if r.status_code != 200:
   print r.status_code
   exit()
else:
    data = json.loads(r.text)

c = data['rollup_history'][0]

print "\nOverview info: \n Overall Compliance Percentage", c['compliance_percentage'], " Total Computer Groups: ", c['total_vulnerable'], "\n"
print "Number of Computers in each Compliance Quartile (0-24%, 25-49%, 50-74%, 75-99%, 100%): ", c['count_quartile_0'], c['count_quartile_1'], c['count_quartile_2'], c['count_quartile_3'], c['count_quartile_4'] 

print "\n\nCheck Results History:"
print "Not Applicable: ", c['total_na'], " Not Compliant: ", c['total_failed'], " Excepted (NC)", c['total_excepted_failed'], " Excepted (C): ", c['total_excepted_passed'], " Total Compliant: ", c['total_compliant']

print "\nTotal # Checklists: ", c['count_checks'],  "Total Computers: ", c['count_computers']

print "\nTotal Number of Computers Subscribed to a Vulnerability Site: ", c['count_computers_evaluating_vulnerabilities']

# Note that the following call makes clear that the SCA ReST call uses what are 
#      called 'ampersand' parameters.
desired_info = '&columns[]=name'
baseurl = 'http://tomato/api/scm/computers.json?token=' + token + desired_info

r = requests.get(baseurl)

# check to see if the server responded appropriately
if r.status_code != 200:
   print r.status_code
   exit()
else:
    data = json.loads(r.text)

# The information received back from SCA is in what's called 
#     JSON (javascript object notation, a human-readalble format 
#     text-format which looks something like a C++ 'struct' construct.
#     We 'pull the data' into a PYTHON dictionary, so we can manipulate 
#     it and print it out in a way that makes sense to a non-programmer
#     human. See, below:
print "\nNames of machines in SCA group follow:" 
myList = []
for eachName in data['rows']:
    myList.append(eachName['name'])

print ', '.join(myList)


