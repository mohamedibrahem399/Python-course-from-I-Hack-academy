#!/usr/bin/python


import subprocess
import optparse

parser=optparse.OptionParser()	#init the parser object
parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
#adding the options like -i or --interface switches, dest this where the passed values get saved and help display the help msg python macchanger.py --help

parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")

(options,arguments)=parser.parse_args()	
#the funtion returns a value to this 2 varible options and arguments
#options is nobut the wlan0 and aa:bb:cc:dd:ee:ff
#arguments is nothingbut --interface and --mac or -i and -m

interface = options.interface
macaddr = options.new_mac

#options contains the value to get the value we call options.interface and options.new_mac

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
subprocess.call(["ifconfig",interface,"up"])

print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)