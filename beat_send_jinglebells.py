#!/usr/bin/python2.7

import socket
import time as t

UDP_IP = "0.0.0.0"
UDP_PORT = 8009
MESSAGE = "Hello Robot!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

i = 0

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
sock.settimeout(0.2)
sock.bind(("",UDP_PORT))


BEAT_CURRENT = 1
BEAT_MAX = 4
BEAT_SUB = 1
MESSAGE = " "

def doBeat(bpm):
  global BEAT_CURRENT, BEAT_SUB, BEAT_MAX, MESSAGE
  T = 1/(bpm/60.0)/4.0
  MESSAGE = str(BEAT_CURRENT) + " " + str(BEAT_SUB) + " " + str(BEAT_MAX)
  sock.sendto(MESSAGE, ('<broadcast>', UDP_PORT))
  #sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
  BEAT_SUB +=1
  if(BEAT_SUB > 4):
    BEAT_SUB = 1
    BEAT_CURRENT += 1
    if(BEAT_CURRENT > BEAT_MAX):
      BEAT_CURRENT = 1
  t.sleep(T)

i = 0
while True:
  doBeat(90)
  print MESSAGE

