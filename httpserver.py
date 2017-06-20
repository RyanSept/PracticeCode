import myhttpsimpleserver as SimpleHTTPServer
import SocketServer
import os
import urllib
p=[]
def get_files():
    d=u"/D_Drive/Users/user/Desktop/PICTURES/Internet pics/"
    foo=os.listdir(d)
    for f in foo:
        p.append(d+"/"+f)

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    flag = 1

    def log_message(self, format, *args):
        print "%s - - [%s] %s\n" %(self.address_string(),
                                   self.log_date_time_string(),
                                   urllib.unquote(format%args).decode('utf8'))

Handler = MyHandler
server = SocketServer.TCPServer(("0.0.0.0",9999),Handler)
server.allow_reuse_address=True
os.chdir("/")
server.serve_forever()
