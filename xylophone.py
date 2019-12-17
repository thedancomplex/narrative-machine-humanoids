import narrative_machine_tmp as nm
import time
import random as r
import rospy
import numpy as np
from std_msgs.msg import String
#pub = rospy.Publisher('play_note', String, queue_size=10)
#rospy.init_node('talker', anonymous=True)

joint = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
RSP = 1
LSP = 2
REP = 5
LEP = 6
RSR = 3
LSR = 4

nm.init()

nm.vel(0,100)

def deg2rad(dvel):
  return dvel*np.pi/180.0


def test():
  for i in range (nm.NUM_JOINTS):
    nm.set(i,0.1)

#nm.home()
#nm.put()
#time.sleep(1.0)
#nm.set(LEP,-3.14/8.0 + 0.35) # + out
#nm.set(REP,3.14/9.0)
#nm.set(11,-.2)
#nm.set(12,.2)
#nm.put()
#time.sleep(3)
#nm.set(1,-3.14/6.0)
#nm.set(2,3.14/6.0)
#nm.put()
i=0

ts = 0.1

def zero():
  for i in range (nm.NUM_JOINTS):
    nm.set(i,0.0)


def home():
  #nm.set(RSP,-3.14/6.0)
  #nm.set(LSP,3.14/6.0)
  #nm.set(REP,3.14/9.0)
  #nm.set(LEP,-3.14/8.0)
  nm.put()

def playB():
  nm.set(5,3.14/9.0)
  nm.set(1,-3.14/3.9)

def playF():
  nm.set(6,-3.14/9.0)
  nm.set(2,3.14/4.1)

def playA():
  nm.set(5,3.14/7.0)
  nm.set(1,-3.14/3.8)

def playG():
  nm.set(6,-3.14/7.0)
  nm.set(2,3.14/4.0)

def playBF():
  nm.set(5,3.14/9.0)
  nm.set(6,-3.14/9.0)
  nm.set(1,-3.14/3.9)
  nm.set(2,3.14/4.1)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    if(data.data == "C4"):
      playC4()
    elif(data.data == "D4"):
      playD4()
    elif(data.data == "E4"):
      playE4()
    elif(data.data == "F4"):
      playF4()
    elif(data.data == "G4"):
      playG4()
    elif(data.data == "A5"):
      playA5()
    elif(data.data == "B5"):
      playB5()
    nm.put()

def playC5():
  global joint
  joint[RSP] = -3.14/6.0 + 0.3
  nm.set(RSP,joint[RSP])
  nm.set(REP,-3.14/9.0)
  print "C2"

def playF3():
  global joint
  joint[LSP] = 3.14/6.0 #- 0.2
  nm.set(LSP,joint[LSP])
  nm.set(LEP,-3.14/8.0 + 0.35)
  #nm.set(LSR,-3.14/4.0 - 0.7)
  print "F3"

def playPose():
  nm.set(nm.LSR,deg2rad(-45.0))
  nm.set(nm.RSR,deg2rad(45.0))
  nm.set(nm.REP,deg2rad(-45.0))
  nm.set(nm.LEP, deg2rad(-45.0))
  nm.set(nm.RSP, deg2rad(-45.0))
  nm.set(nm.LSP, deg2rad(-45.0))

def doBeat(hand):
  if(hand == "L"):
    da = 0.1
    nm.set(LSP, joint[LSP] + da)
    nm.put()
  elif(hand == "R"):
    da = -0.1
    nm.set(RSP, joint[RSP] + da)
    nm.put()
  elif(hand == "B"):
    da = 0.1
    nm.set(LSP, joint[LSP] + da)
    da = -0.1
    nm.set(RSP, joint[RSP] + da)
    nm.put()
  time.sleep(1.0)
  nm.set(LSP, joint[LSP])
  nm.set(RSP, joint[RSP])
  nm.put()
  time.sleep(1)
#home()
#while(True):
rospy.init_node('listener', anonymous=True)
rospy.Subscriber("play_note", String, callback)
print "ready"
#home()
#nm.put()
#playC5()
#playF3()
playPose()


#zero()
#nm.put()
#time.sleep(3.0)
#doBeat("L")
#doBeat("R")
#doBeat("B")
rospy.spin()
#  cur,sub,maxBeat = nm.beat()

#nm.home()
nm.put()
