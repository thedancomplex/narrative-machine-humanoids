#!/usr/bin/python2.7

import socket
import time as t

UDP_IP = "192.168.8.255"
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
while True:
  sock.sendto(MESSAGE, ('<broadcast>', UDP_PORT))
  #sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
  print i
  i += 1
  t.sleep(1.0)

