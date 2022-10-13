#!usr/bin/python2.7
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
iana = ('whois.iana.org', 43)
t = sys.argv[1]

s.connect(iana)
s.send(t + "\r\n")
response = s.recv(1024).split()
#print referer
for i in range(0, len(response)):
	if response[i] == 'refer:':
		referer = response[i+1]
		break
s.close()

rir = (referer, 43)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(rir)
s.send(t + "\r\n")
response = s.recv(1024)
print response
