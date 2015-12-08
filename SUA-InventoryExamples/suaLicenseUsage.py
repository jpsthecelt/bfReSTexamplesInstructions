
## Now, using the computer-name/ID mapping, let's query for some 'software instance usage'; i.e. computer-name and software-titles installed on that machine
##      as well as how often that software was used.
#oi = overviewInfo + lu
#ovUrl = oi + '?token=' + token + '&columns[]=computer_system_id&columns[]=metric_name&columns[]=peak_value&columns[]=software_title_dimension.name' + ul
##'&columns[]=computer_system_id&columns[]=catalog_dimension.software_title_name' + ul
##+ '&limit=100000&offset=100000'
#
#r = requests.get(ovUrl,verify=False,auth=('bigfix','bigfix'))
#
## check to see if the server responded appropriately
#if r.status_code != 200:
#   print r.status_code
#   exit()
#else:
#    data = json.loads(r.text)
#
#print "\nSoftware Usage: "
## print out the computer and installed software
#for c in data['rows']: 
#    if c['computer_system_id'] is not None:
#        print "\n", 
#        print "Computer System ID: ", c['computer_system_id'], "/", c['metric_name'], ": ", c['software_title_dimension']['name'], "Peak Value: ", c['peak_value']
##computerList[c['computer_system_id']],  
#print "\nThen end."
##https://9.39.122.183:9081/sam/software_aggregates/140365/software_aggregates#a40d38b1841e9232c5c65b0310e206f82a63d037
