#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib
import datetime
import getopt
import sys

def usage():
	print "luas.py [-i] [-o] [-l location]"



def main(argv):
	try:
		opts, args = getopt.getopt(argv, "oil:")
	except getopt.GetoptError:           
		usage()
		sys.exit(2)

	location = "Abbey+Street"
	direction = 'outgoing'
	for opt, arg in opts:
		if opt == '-i':
			direction = 'incoming'
		elif opt == "-l":
			location = arg


	webpage = urllib.urlopen('http://www.luas.ie/luaspid.html?get=%s'%location)
	data = webpage.read()
	soup = BeautifulSoup(data)
	incomingDiv = soup.find("div","Inbound")
	outgoingDiv = incomingDiv.findNextSibling('div')

	if direction == 'incoming':
		directionDiv = incomingDiv
	else:
		directionDiv = outgoingDiv

	divcontents = []
	for x in directionDiv.findAll('div'):
		divcontents.append(x.contents[0])

	#pair the destination and the ETA
	outgoingTimes = zip(divcontents[::2], divcontents[1::2])

	for dest,mins in outgoingTimes:
		if mins.isdigit():
			esttime = (datetime.datetime.now() + datetime.timedelta(minutes=int(mins))).strftime("%I:%M %p")
		else:
			esttime = ""
		print dest,mins,'\t',esttime
	

if __name__ == "__main__":
	main(sys.argv[1:])
