#!/usr/bin/python2.7

import socket
import time as t

UDP_IP = "192.168.8.255"
UDP_PORT = 8010
MESSAGE = "Hello Robot!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
sock.settimeout(0.2)
sock.bind(("",UDP_PORT))

def set(mot, val):
  # val is float to represent the joint angle in radians
  toSend = "M"+str(mot) + "A" + str(val).encode()
  sock.sendto(toSend,('<broadcast>',UDP_PORT))
  # Set motor and angle value for joint
  # Ready to be sent (but not sent)

def put():
  toSend = "P"
  sock.sendto(toSend,('<broadcast>',UDP_PORT))
  # put all set values on to the robot

"""
def get():
  # get current angle values of robot
def init():
# initilize the dyn package
# also initializes network settings

def close():
# stops the dyn packs
"""

def home():
  toSend = "H"
  # sets robot to home position
  sock.sendto(toSend,('<broadcast>', UDP_PORT))
  
def vel(mot,vel):
  toSend = "M"+ str(mot) + "V" + str(vel).encode()
  sock.sendto(toSend,('<broadcast>', UDP_PORT))
  # set velocity for mot at vel(deg/sec)

def twistArms():
  vel(0,750)
  i = 0
  while(i < 3):
    set(2,-3.14/2.0)
    set(1,-3.14/2.0)
    put()
    t.sleep(1.0)
    set(1,3.14/2.0)
    set(2,3.14/2.0)
    put()
    t.sleep(1.0)
    i+=1

def flexArms():
  vel(0,1023)
  i=0
  while(i < 3):
    set(5,0.0)
    set(6,0.0)
    put()
    t.sleep(1.0)
    set(5,-3.14/2.0)
    set(6,3.14/2.0)
    put()
    t.sleep(1.0)
    i+=1

def flexInvertArms():
  vel(0,1023)
  i=0
  while(i < 3):
    set(5,-3.14/2.0)
    set(6,0.0)
    put()
    t.sleep(1.0)
    set(5,0.0)
    set(6,3.14/2.0)
    put()
    t.sleep(1.0)
    i+=1

def doubleArms():
  vel(0,1023)
  i=0
  while(i < 3):
    set(2,-3.14/2.0)
    set(1,-3.14/2.0)
    set(5,0.0)
    set(6,0.0)
    put()
    t.sleep(1.0)
    set(5,-3.14/2.0)
    set(6,3.14/2.0)
    set(1,3.14/2.0)
    set(2,3.14/2.0)
    put()
    t.sleep(1.0)
    i+=1

"""def beat()
# block until next beat
# return an int as to where in the measure we are
"""
set(12,-3.14/2.0)
#home()

#put()
#i = 0

#t.sleep(3.0)
#j = 0
#t.sleep(2.0)
#while(j < 3):
#  twistArms()
#  flexArms()
#  flexInvertArms()
#  doubleArms()
#  j+=1

#t.sleep(2.0)
#home()
#put()
"""
while(i < 10):
  set(2,-3.14/2.0)
  set(1,-3.14/2.0)
  put()
  t.sleep(1.0)
  set(1,3.14/2.0)
  set(2,3.14/2.0)
  put()
  t.sleep(1.0)
  i+=1
"""
"""
while(i < 3):
  set(4,-3.14/8.0)
  set(3,3.14/4.0)
  put()
  t.sleep(2.0)
  set(4,-3.14/4.0)
  set(3,3.14/8)
  put()
  t.sleep(2.0)
  i+=1
home()
put()"""
