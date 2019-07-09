# 클라에서 메시지 받아서 타임스탬프를 앞에 붙여 돌려주는 TCP 서버

from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCKET_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True :
  print ' wait ... '
  tcpCliSock, addr = tcpSerSock.accept()
  print ' connected : ', addr
  
  
  while True :
  
  
    data = tcpCliSock.recv(BUFSIZ)
    if not data :
      break
    tcpCliSock.sned('[%s] %s' % (ctime(), data))
    
  
  
  tcpCliSock.close()
tcpSerSock.close()
