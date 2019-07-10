# socketserver tcp sever... 단순화된 서버작업

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime


HOST = ''
PORT =21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH) :
  def handle(self) :
    print '...connected from : ', self.client_address
    self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline().strip()))


tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection....'
tcpServ.serve_forever()
