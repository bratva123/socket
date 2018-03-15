#!/usr/bin/python

import socket
import commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",1099))
while 4>3 :
   data=s.recvfrom(200) 
   y=commands.getoutput('which '+data[0]+' | grep -io '+data[0])
   print y 
   z=commands.getoutput('enable -a | cut -d " " -f 2,3 | grep -i '+data[0]) 
   if y==data[0] :
        print "acepted",data[0]
        s.sendto("accepted...",data[1])
   elif z==data[0]:
        print "acepted",data[0]
        s.sendto("accepted...",data[1])
   else:
        s.sendto("rejected...",data[1])
s.close()
