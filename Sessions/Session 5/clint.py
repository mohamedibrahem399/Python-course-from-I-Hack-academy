import socket 
import sys 
import subprocess
import time


sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


server_address = ('192.168.0.101',9988)

print ("connecting up on %s port %s " % server_address)

time.sleep(2)
sock.connect(server_address)

try:
	message = input(r"send: ")

	print ('sending"%s"'% message )
	sock.sendall(message.encode())
	time.sleep(2)

	amount_received =0
	amount_expected =len(message)
	
	while amount_expected < amount_expected :
		data =sock.recv(32)
		amount_received += len(data)
		print ('received"%s"'% data )
		time.sleep(2)
finally :
	print ('closing socket')
	sock.close()

