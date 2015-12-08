#import pdb # used for debugging
import json
import requests
#
# Author: John Singer, Channels BigFix CTP
# Purpose: As an educational-resource for both customers and CTPs, to learn
#          how to extract SCA report information via ReST.
#
# Note that for this exercise, you must login into the SCA reports, go to 
#      the Account/preferences/Show token screen of SCA, to grab the SSL 
#      token and use it as indicated, below
# $Id$:
#
token = '137806544748ddbf083d7849cbfecf8a7fb41bc2'

# Note that SCA ReST queries are set up as 'ampersand' parameters, connected
#      together, as you can see, below:
desired_info = '&columns[]=name&columns[]=rollup.count_checks&columns[]=rollup.total_passed&columns[]=rollup.total_excepted_passed&columns[]=rollup.total_excepted_failed&columns[]=rollup.total_failed&columns[]=rollup.total_na&columns[]=rollup.total_compliant'

# using 'ampersand' URL-parameters, specify 'baseURL, the token, and the 
#       other detaikls of desired information
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
print "\nNames and rollup-counts of machines in SCA group:\n"
for name in data['rows']:
    print "name: ", name['name'],  "\nrollup: total_failed, count_checks, total_na, total_compliant, total_passed, total_excepted_failed, total_excepted_passed:\n\t"
    rollup = name['rollup']
    print "\t", rollup['total_failed'], "\t\t", rollup['count_checks'], "\t\t", rollup['total_na'], "\t\t", rollup['total_compliant'], "\t\t", rollup['total_passed'], "\t\t", rollup['total_excepted_failed'], "\t\t", rollup['total_excepted_passed'], "\n"
