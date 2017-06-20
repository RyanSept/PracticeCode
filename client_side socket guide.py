# Create a socket object

# Get local machine name

# Reserve a port for your service.

# Close the socket when done
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 2526                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close()      
