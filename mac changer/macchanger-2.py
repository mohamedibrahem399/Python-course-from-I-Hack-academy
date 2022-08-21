#!/usr/bin/python


import subprocess

interface = "wlan0"
macaddr = "00:11:22:33:44:55"

print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)


subprocess.call("ifconfig %s down"%interface,shell=True)
subprocess.call("ifconfig %s hw ether %s"%(interface,macaddr),shell=True)
subprocess.call("ifconfig %s up"%interface,shell=True)