import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #open a socket, sock_stream is for tcp connections d_gram for udp
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host=socket.gethostbyname_ex(socket.gethostname())[2][0]
port=3036
s.bind((host,port))
print "Opened connection on",host,port
while True:
    s.listen(5)
    conn,addr=s.accept()
    print conn,addr,"connected"
    result=conn.recv(4096)
    if result=='close':
        conn.close()
        s.close()
    else:
        exec(result)
    result=conn.recv(4096)
##while len(result)>0:
##    print result
##    result=s.recv(1024)
