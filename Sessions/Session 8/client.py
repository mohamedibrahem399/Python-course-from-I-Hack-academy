import socket
import sys
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.0.137', 9988)
print('connecting to %s port %s' % server_address)
time.sleep(2)
sock.connect(server_address)
try:
    
    # Send data
    message = input(r"send: ")
    print('sending "%s"' % message)
    sock.sendall(message.encode())
    time.sleep(2)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(32)
        amount_received += len(data)
        print('received "%s"' % data)
        time.sleep(2)

finally:
    print('closing socket')
    sock.close()