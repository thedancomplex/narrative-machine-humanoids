import narrative_machine_tmp as nm
import time
import random as r

import sys
import select
import tty
import termios
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',8888))
s.setblocking(0)
data =''
address = ''


def isData():
 print 'here 1'
 try:
  print 'here 2'
  data,address = s.recvfrom(1)
  print 'here 3'
  return 1
 except socket.error:
  return 0
  pass
 else:
  print "recv:", data[0],"times",len(data)
  return 0
	



nm.init()

nm.vel(0,1023)
nm.home()
nm.put()
time.sleep(1.0)
nm.set(6,-3.14/9.0)
nm.set(5,3.14/9.0)
nm.put()
time.sleep(0.5)
nm.set(1,-3.14/4.0)
nm.set(2,3.14/4.0)
nm.put()
i=0

drumState = 1

def doDrum():
  global drumState
  if(drumState == 1):
    nm.set(1,-3.14/6.0)
    nm.set(2,3.14/4.0)
    drumState = 0
  else:
    nm.set(1,-3.14/4.0)
    nm.set(2,3.14/6.0)
    drumState = 1

while(True):
  cur,sub,maxBeat = nm.beat()
  if( isData() == 1):
    print 1
    doDrum()
  elif(sub==1):
    doDrum()
  
  nm.put()

nm.home()
nm.put()
