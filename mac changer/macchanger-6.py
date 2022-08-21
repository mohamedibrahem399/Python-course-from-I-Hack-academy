#!/usr/bin/python


import subprocess
import optparse


def macchanger(interface,macaddr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
	subprocess.call(["ifconfig",interface,"up"])

	print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)

parser=optparse.OptionParser()	
parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")
(options,arguments)=parser.parse_args()	

macchanger(options.interface,options.new_mac)

