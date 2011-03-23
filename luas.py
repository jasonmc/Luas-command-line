#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib
import datetime



webpage = urllib.urlopen('http://www.luas.ie/luaspid.html?get=Abbey+Street')
data = webpage.read()


soup = BeautifulSoup(data)


incomingDiv = soup.find("div","Inbound")


outgoingDiv = incomingDiv.findNextSibling('div')


k = []
for x in outgoingDiv.findAll('div'):
	k.append(x.contents[0])


outgoingTimes = zip(k[::2], k[1::2])


for t in outgoingTimes:
	dest = t[0]
	mins = t[1]
	

	if mins.isdigit():
		esttime = (datetime.datetime.now() + datetime.timedelta(minutes=int(mins))).strftime("%I:%M %p")
	else:
		esttime = ""

	print dest,mins,'\t',esttime
	
