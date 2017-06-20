import socket
import sys

host=''
port=867

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:   #capture the error as var e
    print str(e) #print the error

s.listen(5)     #will be listening on port 5555, 5 is the max number of connections to allow in queue

conn, addr=s.accept()

print 'connected to: '+addr[0]+':'+str(addr[1])
