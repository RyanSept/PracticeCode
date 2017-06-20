# Import socket module

# Create a socket object

# Get local machine name

# Reserve a port for your service.

# Bind to the port

# Now wait for client connection.

 # Establish connection with client.

# Close the connection

import socket               # Import socket module
import os
s = socket.socket()         # Create a socket object
host = socket.gethostbyname_ex(socket.gethostname())[2][0] # Get local machine name
port = 2515 # Reserve a port for your service.
print host
try:
    s.bind((host, port))        # Bind to the port
except socket.error as e:
    s.close()
    print str(e)
    if str(e)=='[Errno 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted':
        s.bind((host,port+20))

s.listen(5)# Now wait for client connection.

c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
with open('D:/ryan music/The Weight Lifted -Ezekiel.mp4','rb') as pic:
    for data in pic:
        c.sendall(data)
print 'end'
c.close()
s.close()
