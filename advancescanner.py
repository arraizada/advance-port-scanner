#!/usr/bin/python

from socket import *
import optparse
from threading import *

def ConnScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect ((tgtHost, tgtPort))
		print '[+] %d/tcp Open' %tgtPort
	except:
		print '[-] %d/tcp closed' %tgtPort
	finally:
		sock.close()

def PortScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print 'Unknown Host %s' %tgtHost
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '[+] Scan Results For: ' + tgtName[0]
	except:
		print '[+] Scan Results For: ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=ConnScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('usage of Program: ' + '-H <target Host> -P <target Port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target Host')
        parser.add_option('-P', dest='tgtPort', type='string', help='specify target Port separated bt comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)

	PortScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()

