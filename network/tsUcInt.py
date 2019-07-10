# udp 클라이언트

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUSFIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True :
  data = raw_input('> ')
  if not data :
    break
  udpCliSock.sendto(data, ADDR)
  
  data, ADDR = udpCliSock.recvfrom(BUFSIZ)
  if not data :
    break
  print data


udpCliSock.close()
