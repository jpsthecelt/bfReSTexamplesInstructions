import urllib,urllib2
baseurl="http://grasskeet:52311/"

# enable password management on URL access
pwdMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# supply the necessary credentials & supply handler & build/install
#        the URL opener
pwdMgr.add_password(None,baseurl,'adminMO','adminmo')
auth = urllib2.HTTPBasicAuthHandler(pwdMgr)
opener = urllib2.build_opener(auth)
urllib2.install_opener(opener)

#opener.open(baseurl+'query?relevance=now')
#opener.open(baseurl)
#loginUrl = 'http://localhost:52311/api/login'
#response = urllib2.urlopen(loginUrl)
relevance = '(name of fixlet of it) of results from (bes fixlets whose (display name of site of it contains "Patches for RHEL 5" and fixlet flag of it = true)) whose (exists last became relevant of it and relevant flag of it = false) of bes computers whose (name of it as lowercase contains "adonix")'

mr = baseurl+'api/query?relevance='+urllib.quote(relevance)

print 'quoted url is: ', mr
response = urllib2.urlopen(mr)
print 'response is: ', response

myRequest = baseurl+'api/query?relevance='+relevance
print 'request URL is:', myRequest
#response = urllib2.urlopen('http://grasskeet:52311/api/query?relevance=now')
response = urllib2.urlopen(myRequest)

for line in response.readlines(): print line,
#the_page = response.read()
#print the_page
