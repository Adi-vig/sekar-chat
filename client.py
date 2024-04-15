import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 6667)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# # Send data
# message = b'NICK bot\r\n'
# print('sending {!r}'.format(message))
# sock.sendall(message)

# message = b'USER bot bot bot :Python IRC Bot\r\n'
# print('sending {!r}'.format(message))
# sock.sendall(message)

# message = b'JOIN #python\r\n'
# print('sending {!r}'.format(message))
# sock.sendall(message)

message = b'PRIVMSG #python :Hello World!\r\n'
# print('sending {!r}'.format(message))
sock.sendall(message)

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(1024)
    amount_received += len(data)
    print('received {!r}'.format(data))

print('closing socket')
sock.close()
