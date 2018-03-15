#!/usr/bin/python

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4>3 :
   x=raw_input("[hello.......]   ")
   s.sendto(x,("127.0.0.1",10871))
   print s.recvfrom(200)
s.close()
