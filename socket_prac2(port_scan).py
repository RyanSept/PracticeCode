import socket
import threading
from Queue import Queue

print_lock=threading.Lock()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server='verselists.wordpress.com'

def port_scan(port):
    try:
        con=s.connect((server,port))
        with print_lock:
            print 'port',port,'is open!!!!!!!!!!!!!!'
        con.close()
    except:
        pass
port_scan(80),port_scan(22120)
def threader():
    while True:
        worker=q.get()
        port_scan(worker)
        q.task_done()
q=Queue()

for x in range(30):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()
for worker in range(1,101):
    q.put(worker)
q.join()
##for x in range(1,26):
##    if port_scan(x):
##        print 'Port %d is open'%(x)
##    else:
##        print 'Port %d is closed'%(x)
