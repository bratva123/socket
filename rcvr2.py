#!/usr/bin/python

import socket
import commands
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",10871))
while 4>3 :
   data=s.recvfrom(200) 
   y=commands.getoutput('which '+data[0]+' | grep -io '+data[0])
   z=commands.getoutput('enable -a | cut -d " " -f 2,3 | grep -i '+data[0]) 
   if y==data[0] :
        print "acepted",data[0]
        v=commands.getoutput(y)
        s.sendto(v,(data[1]))
   elif z==data[0]:
        print "acepted",data[0]
        t=commands.getoutput(z)
        s.sendto(t,(data[1])) 
   else:
        s.sendto("rejected...",data[1])
s.close()
