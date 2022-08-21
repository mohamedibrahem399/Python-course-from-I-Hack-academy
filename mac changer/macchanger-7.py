#!/usr/bin/python


import subprocess
import optparse


def macchanger(interface,macaddr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
	subprocess.call(["ifconfig",interface,"up"])

	print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)

def get_argument():
	parser=optparse.OptionParser()	
	parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
	parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")
	return parser.parse_args()	

(options,arguments) = get_argument()
macchanger(options.interface,options.new_mac)

