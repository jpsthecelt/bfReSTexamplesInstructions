BF-ReST-InstructionExamples
Some ReST examples I created for client-instruction, partners, interested parties, etc.

Thanks for reading.... jps


____________________________________________________________________________________________________
LESSON 2:

Greetings, folks; jpsthecelt, here. 'Sales Engineer to the Stars'.

Since I've been 'up to my eyeballs' helping customers, I've never gotten to adding my bit on ReST, so here 'tis.

Been programming for about 30 years, now, and working with BigFix for the last 7; so I've developed a simplified perspective after 'sifting' through a lot of the examples we've seen, so far.

I recently read the bit that GTaylor added, which was great, and thought I'd share some of the examples from the series of ReST lessons I developed for a large entertainment company.

I've developed largely in Python, for it's clarity & ease of understanding. I've also included an example in Ruby, and will eventually add my Java & Perl examples; the point being, that the language doesn't matter, since it's all CRUD (create, read, update, delete), courtesy of the ability to 'transfer state' (information) via a simplified 'representation' (REST - Representational State Transfer).

So, let's talk about your testing setup.  I work a lot with Windows, but I'm a former Unix guy, so I use a lot of commandline tools.  Installing CygWin makes the transition between the two pretty seamless, and immediately provides tools like Python, Ruby, Curl, and wget.

Although interpreted languages are prone to type-mismatch bugs, they're extremely easy to use and one can create working code in a minimum of time; hence, Python, Ruby, etc. 

Another thing I should note; in a production environment, one would probably use certificates or a central authentication service/repository, but I have simplified authentication for the sake of brevity and clarity (We will see my use of certificates in a later lesson).

So, let's look at some examples.

Examples & explanations -- Lesson 
----------------------------------

Here are some examples in two of those languages, Python and Ruby (I'm using the vanilla BF ReST api, but the same can be done with the SCA (security) and SUA ReST apis). For Ruby, we'll use net/http (libraries in Python are called 'eggs'; ruby libraries are called 'gems').

The first thing to notice about these programs is that they use HTTP/ReST libraries which make authentication and interface much easier.  In the case of Python,
The library is called Requests, which you can get here (as well as install instructions):
https://pypi.python.org/pypi/requests

Once installed, you use it by referencing requests  as one of the first lines in your script, i.e.
Import requests

Given this library, access to the BigFix ReST api is very simple: Besides setting up the connection, there are two commands which you will need to script,
The 'login' and the 'get' or 'put'. Using the Request library you have a login (& status check) like:

r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

Notice that the requests.get line says 'verify=False'. This is so you don't have to present a certificate, and I used it to simplify this demo/instruction.
My login username was 'adminMO' and my password was 'adminmo'.

The login checks the return status code & prints it if it is not successful (i.e.200).

So, if we then wanted to query all the fixlets within the 'BES Support' site, we could issue the following 'get':
baseurl = 'https://localhost:52311/api/'
r = requests.get(baseurl+'fixlets/external/BES Support',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

Now, in this example, I added other code to be able to parse the returned XML and display fixlet ID numbers followed by the name of the fixlets.
(I also used a default python library called ElementTree, included in the Python 5.10 distribution, which facilitates parsing and creating a dictionary. Once the XML is parsed into a dictionary, it's very straightforward to print it out, as seen in the code, below):


Running this script (with 'less' so I only see one screen at a time), would look like:
Python temRest.py | less
starting search in results
creating dictionary
try to print dict
1524 Updated ESX Client - Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
1525 Updated HP-UX Client - Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
1526 Updated Mac OS X Client - i386/PPC - Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
1527 Updated Red Hat Enterprise 3 Client - i686 - Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
1252 Updated Mac OS X Client - i386/PPC - Tivoli Endpoint Manager version 8.2.1364.0 Now Available!
1521 Updated AIX 6.1 Based Relay - PPC64 - Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
1798 IBM Endpoint Manager - Updated Platform Server Components version 9.1.1117.0 Now Available!
1522 Updated Debian 5 Client - i686 - Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
719 Updated BigFix BES API Now Available! (Version 8.0.627.0)
718 Updated AIX BES Client Now Available! (Version 8.0.627.0)
1793 WARNING: Critical Security Vulnerability in 8.1 (Web Reports Server, Server API)
716 Adobe Flash Player Required - BES Console
715 Mac Firewall is Blocking BES Traffic (OS X 10.6)
1523 Updated Debian 5 Client - x86_64 -Tivoli Endpoint Manager version 8.2.1409.0 Now Available!
1797 Updated Windows Proxy Agent - IBM Endpoint Manager version 9.0.40099 Now Available!
711 WARNING: BigFix agent may require regedit.exe to operate properly on Windows
1794 Updated Windows Proxy Agent - IBM Endpoint Manager version 9.1.1117.0 Now Available!
1490 Updated Ubuntu 8 Client - i686 - Tivoli Endpoint Manager version 8.2.1400.0 Now Available!
1491 Updated Ubuntu 8 Client - x86_64 - Tivoli Endpoint Manager version 8.2.1400.0 Now Available!
1494 Updated Windows Client - Tivoli Endpoint Manager version 8.2.1400.0 Now Available!
:
Here's the source code:


import requests
import xml.etree.ElementTree as ET

baseurl = 'http://localhost:52311/api/'

r = requests.get('http://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

baseurl = 'https://localhost:52311/api/'

r = requests.get(baseurl+'fixlets/external/BES%20Support',verify=False,auth=('adminMO','adminmo'))

if r.status_code != 200:
   print r.status_code

root = ET.fromstring(r.text)

i = []
n = []
print 'starting search in results'
for fixlet in root.findall('Fixlet'):
   n.append(fixlet.find('Name').text)
   i.append(fixlet.find('ID').text)
print 'creating dictionary'
d = dict(zip(i,n))

print 'try to print dict'
for key in iter(d):
   print key,d[key]


**************************

Update, as of 1.17.15-jps:

> I recently updated my development environment, and found that there was a new version of the requests library which 'throws' a warning when you neglect to use a real SSL certificate. This looks ugly, even for testing.  As a result, I recoded the above example, using urllib3, which just happens to have a 'disable_warnings()' routine that makes testing easier & prettier.  This following code produces exactly the same result as shown above.

So, now, I used the following code -- notice it's completely the same, except for the urllib3 calls vs. the requests calls, and I think it looks more 'self-documenting'.

(Oh, yeah, there's another trivial difference, in that urllib3 has a r.data vs. an r.text attribute and r.status vs. an r.status_code attribute):


import urllib3
import xml.etree.ElementTree as ET
baseurl = 'http://grasskeet:52311/api'
http = urllib3.PoolManager()
url = baseurl + '/login'
headers = urllib3.util.make_headers(basic_auth='adminMO:adminmo')
urllib3.disable_warnings()
r = http.request('GET', url, headers=headers)
if r.status != 200:
   print r.status
url = baseurl+'/fixlets/external/BES%20Support'
headers = urllib3.util.make_headers(basic_auth='adminMO:adminmo')
urllib3.disable_warnings()
r = http.request('GET', url, headers=headers)
if r.status != 200:
   print r.status
if r.status != 200:
   print r.status
root = ET.fromstring(r.data)
i = []
n = []
print 'starting search in results'
for fixlet in root.findall('Fixlet'):
   n.append(fixlet.find('Name').text)
   i.append(fixlet.find('ID').text)
print 'creating dictionary'
d = dict(zip(i,n))
print 'try to print dict'
for key in iter(d):
   print key,d[key]

**************************



I have two other useful scripts, one will import a fixlet called 'TweedleDee' into the BF master action site.
Again, I have a line that logs me in, and another that does a POST:

r = requests.post(baseurl+'fixlets/master',verify=False,auth=('adminMO','adminmo'), data=open('TweedleDee.bes','rb'))
if r.status_code != 200:
   print r.status_code

ImportTweedelDeeFixlet.py and TweedleDee.bes (which I originally got by exporting an existing fixlet) look like the following (ImportTweedleDeeFixlet.py, first):
# With this script, we're going to take an exported fixlet, 'TweedleDee.bes' and import it into the console using the ReST API.

# notice that this uses the Python Egg called Requests;
#    it simplifies REST authentication, such that I can easily specify the URL,
#    the fact that I'm bypassing any SSL Cert, and my username/password.

import requests
import xml.etree.ElementTree as ET

baseurl = 'https://localhost:52311/api/'

# open saved fixlet XML file
files = {'file': open('TweedleDee.bes', 'rb')}

# Login to REST Api...
r = requests.get('https://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

# Now POST the fixlet to the master action site (.../fixlets/master)
#    it'll 'show up' in the console, under 'my custom content'
r = requests.post(baseurl+'fixlets/master',verify=False,auth=('adminMO','adminmo'), data=open('TweedleDee.bes','rb'))

if r.status_code != 200:
   print r.status_code
print 'Heres the XML I got back from POSTing', r.text


Second, the exported (XML) contents of TweedelDee.bes:


<?xml version="1.0" encoding="UTF-8"?>
<BES xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BES.xsd">
    <Fixlet>
        <Title>Tweedle-Dee Tweedle-dum</Title>
        <Description><![CDATA[This task will deploy: DsQueryGetFiles.<BR><BR>This task is applicable on: Windows 2000, Windows XP, Windows XP x64, Windows 2003, Windows 2003 x64, Windows Vista, Windows Vista x64, Windows 2008, Windows 2008 x64, Windows 7, Windows 7 x64 and Windows 2008 R2. ]]></Description>
        <Relevance>(name of it = "Win2000" OR name of it = "WinXP" OR name of it = "WinXP-2003" OR (name of it = "Win2003" AND NOT x64 of it) OR (name of it = "Win2003" AND x64 of it) OR (name of it = "WinVista" AND product type of it = nt workstation product type AND NOT x64 of it) OR (name of it = "WinVista" AND product type of it = nt workstation product type AND x64 of it) OR ((name of it = "Win2008" or (name of it = "WinVista" and product type of it != nt workstation product type)) AND NOT x64 of it) OR ((name of it = "Win2008" or (name of it = "WinVista" and product type of it != nt workstation product type)) AND x64 of it) OR (name of it = "Win7" AND NOT x64 of it) OR (name of it = "Win7" AND x64 of it) OR name of it = "Win2008R2") of operating system AND TRUE</Relevance>
        <Category>Software Distribution</Category>
        <DownloadSize>194116</DownloadSize>
        <Source>Software Distribution Wizard</Source>
        <SourceID></SourceID>
        <SourceSeverity></SourceSeverity>
        <CVENames></CVENames>
        <SANSID></SANSID>
        <MIMEField>
            <Name>x-fixlet-source</Name>
            <Value>Software Distribution Wizard</Value>
        </MIMEField>
        <MIMEField>
            <Name>x-fixlet-modification-time</Name>
            <Value>Wed, 05 Sep 2012 02:02:09 +0000</Value>
        </MIMEField>
        <Domain>BESC</Domain>
        <DefaultAction ID="Action1">
            <Description>
                <PreLink>Click </PreLink>
                <Link>here </Link>
                <PostLink>to initiate the deployment process.</PostLink>
            </Description>
            <ActionScript MIMEType="application/x-Fixlet-Windows-Shell">download http://grasskeet:52311/Uploads/8471b1c90ce1198f36735628585a2a54f6ebd54b/DsQueryGet.tmp
continue if {(size of it = 194116 AND sha1 of it = "8471b1c90ce1198f36735628585a2a54f6ebd54b") of file "DsQueryGet.tmp" of folder "__Download"}

extract DsQueryGet.tmp

if {not exists file "c:\Windows\System32\dsquery.exe"}
move __Download\dsquery.exe "c:\Windows\System32\dsquery.exe"
endif
if {not exists file "c:\Windows\System32\dsquery.dll"}
move __Download\dsquery.dll "c:\Windows\System32\dsquery.dll"
endif
if {not exists file "c:\Windows\System32\dsget.exe"}
move __Download\dsget.exe "c:\Windows\System32\dsget.exe"
endif
if {not exists file "c:\Windows\System32\ds16gt.dll"}
move __Download\ds16gt.dll "c:\Windows\System32\ds16gt.dll"
endif
</ActionScript>
            <SuccessCriteria Option="RunToCompletion"></SuccessCriteria>
        </DefaultAction>
    </Fixlet>
</BES>

*******************************************************

POSTing a message:
Finally, if I want to execute an action (which could be a fixlet or an action-plan), I could create an
XML file with my actionID, and reference it with a BF POST as:
r = requests.post(baseurl+'actions',verify=False,auth=('adminMO','adminmo'), data=open('stopBesGather.xml', 'rb'))


The file temPostActionViaRest.py looks like this:

import requests

baseurl = 'https://localhost:52311/api/'
files = {'file': open('stopBesGather.xml', 'rb')}

r = requests.get('https://localhost:52311/api/login',verify=False,auth=('adminMO','adminmo'))
if r.status_code != 200:
   print r.status_code

# issue action specified in stopBesGather.xml
r = requests.post(baseurl+'actions',verify=False,auth=('adminMO','adminmo'), data=open('stopBesGather.xml', 'rb'))

if r.status_code != 200:
   print r.status_code

print '\nHeres the XML about the action that I got back: \n', r.text


Finally, the same is pretty easily done in any other language, so I've picked Ruby, and I'm using a library (gem) called
Net/http.  The contents of nHTTP.rb is:

require 'net/http'

uri = URI('https://localhost:52311/api/login')

uri2 = URI('http://localhost:52311/api/fixlets/external/BES%20Support')

Net::HTTP.start(uri.host, uri.port,
  :use_ssl => uri.scheme == 'https', :verify_mode => OpenSSL::SSL::VERIFY_NONE) do |http|

  request = Net::HTTP::Get.new uri.request_uri
  request.basic_auth 'adminMO', 'adminmo'

  response = http.request request # Net::HTTPResponse object

  puts response
  puts response.body
end

  Net::HTTP.start(uri2.host, uri2.port,
  :use_ssl => uri.scheme == 'https', :verify_mode => OpenSSL::SSL::VERIFY_NONE) do |http|

  request = Net::HTTP::Get.new uri2.request_uri
  request.basic_auth 'adminMO', 'adminmo'

  response = {}
  response = http.request request # Net::HTTPResponse object

  puts response
  puts response.body
end



This program is invoked as
Ruby nHTTP.rb


As An 'exercise for the student', try using these programs as 'templates', and invoke an automation-plan
From the Server Automation site within BF (assuming that you have IEM with Server Automation).

Enjoy! 'Stay Tuned', and we'll see other stuff 'the cool kids' do....

jps

