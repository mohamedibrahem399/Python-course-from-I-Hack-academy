import socket
import sys 
import time
import subprocess

stock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server_address = ("localhost",10001)

print ("starting up on %s port %s "%server_address)
sock.bind(server_address)
sock.listen(1)

while True :
	print('waiting for a connection')
	time.sleep(2)
	connection , clint_address = sock.accept()

	print ('connection from ',clint_address)

	try:
		while True :
		data =  connection.recv(32)
		response = subprocess.check_output(data,shell=True)
		print ('received"%s"'%data)
		time.sleep (2)
		if data	():
			print('sending data back to client ')
			time.sleep(2)
			connection.sendall(response.decoder())
		else :
			print ('no more data from',clint_address)
			break

	finally:
		connection.close()

