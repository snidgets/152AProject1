# Send 10 pings to server
# Don't wait forever for the server to respond. (WAIT 1 SECOND)
#   if no reply, assume packet loss
# Look up timeout value on a datagram socket

# 1. Send a ping message using UDP
# 2. Print the response from the server, if any
# 3. Calculate and print the round trip time (RTT), in milliseconds of each
#	packet, if the server responds
#	otherwise, print 'Request timed out.' Please use this exact string (with .?)
# Send packets to localhost (127.0.0.1)
# Then test on two different machines
# Test on csif machines
# Change ports if you get the msg "address is already in use"

# Ping message should look like: "Ping sequence_number time"
# sequence number [1:10] and time is when the client sends the message (in ms)
# USE Exact string
from time import clock, strftime, gmtime, localtime
from socket import *
IP = "192.168.1.72"
PORT = 12000
MSGS = []
milli = 1000
sigFigs = 3
setdefaulttimeout(1) # set that timeout to 1 second
#print getdefaulttimeout()
for i in range(1, 11):
	MSGS.append("Ping %d " % i)
client = socket(AF_INET, SOCK_DGRAM)
for message in MSGS:
	junk = strftime("%Y-%m-%d %a %H:%M %Z", localtime())
	#print "Sending %s" % (message+junk)
	sendTime = clock() # dunno bout' this
	client.sendto(message+junk, (IP, PORT))
	try:
		reply, address = client.recvfrom(1024)
		recvTime = clock()
		print reply
		print "RTT: %s" % str((round((recvTime - sendTime)*milli, sigFigs)))
	except timeout:
		print "Request timed out"
# Calculate round trip you bitch
# Problem with out put not match ghosal's i.e T is Tue and PST instead of UTC
# print RTT in ms
