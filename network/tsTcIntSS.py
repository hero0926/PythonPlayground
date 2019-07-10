#socketserver timestamp tcp client

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True :
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  
  data = raw_input('> ')
  if not data :
    break
  tcpCliSock.send(data+'\n')
  
  data = tcpCliSock.recv(BUFSIZE)
  if not data :
    break
  print data
  
  tcpCliSock.close()
