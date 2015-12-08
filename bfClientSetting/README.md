Here's my approach to getting and setting ClientSettings on endpoints...

In this program, I expect that the library requests has been installed, and that the file containing the xml for the client-setting be in the same directory
(settingProto.xml).  It responds to only 3 settings (CF_SystemType, CF_Property1, or CF_Property2), otherwise 'spitting out' the 'help' text (although it
Could be modified to accept any/all others, I figured that a minimalist subset would be more secure). Also note that the target and server names are case-sensitive.

Obtaining the value for CF_SystemType for the server named GRASSKEET & the target GRASSKEET, using my personal test-system credentials adminMO:adminmo would be:
	Python bfClientSetting GRASSKEET -c CF_SystemType -s GRASSKEET adminMO adminmo

Setting the value for CF_Property1  to 52 for the server named GRASSKEET & the target HANHDEPLAM , using the credentials adminMO:adminmo would be:
	Python bfClientSetting HANHDEPLAM -c CF_SystemType -v 52 -s GRASSKEET adminMO adminmo

Hopefully, this may be educational.

	-jps@12.08.15
