#!/usr/bin/python


import subprocess

interface = raw_input("Interface> ")
macaddr = raw_input("MacAddr> ")

print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)


subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
subprocess.call(["ifconfig",interface,"up"])