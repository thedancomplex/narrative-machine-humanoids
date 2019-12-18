import narrative_machine_tmp as nm
import time
import random as r
import rospy
import numpy as np
from std_msgs.msg import String
#pub = rospy.Publisher('play_note', String, queue_size=10)
#rospy.init_node('talker', anonymous=True)

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
  nm.put()

def positionAdjustment():
 playF3()
 playC4()

def home():
  #nm.set(RSP,-3.14/6.0)
  #nm.set(LSP,3.14/6.0)
  #nm.set(REP,3.14/9.0)
  #nm.set(LEP,-3.14/8.0)
  nm.put()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    if(data.data == "F3"):
      playF3()
    elif(data.data == "G3"):
      playG3()
    elif(data.data == "A4"):
      playA4()
    elif(data.data == "B4"):
      playB4()
    elif(data.data == "C4"):
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
    elif(data.data == "C5"):
      playC5()
    elif(data.data == "D5"):
      playD5()
    elif(data.data == "E5"):
      playE5()
    elif(data.data == "F5"):
      playF5()
    elif(data.data == "G5"):
      playG5()
    elif(data.data == "A6"):
      playA6()
    elif(data.data == "B6"):
      playB6()
    elif(data.data == "C6"):
      playC6()
    nm.put()

def playF3():
  nm.set(nm.LSP, deg2rad(47.0))
  nm.set(nm.LEP, deg2rad(-65.0))
  nm.set(nm.LSR, deg2rad(32.0))
  print "F3"

def playG3():
  nm.set(nm.LSP, deg2rad(44.0))
  nm.set(nm.LEP, deg2rad(-69.0))
  nm.set(nm.LSR, deg2rad(32.0))
  nm.put()
  print "G3"

def playA4():
  nm.set(nm.LSP, deg2rad(38.0))
  nm.set(nm.LEP, deg2rad(-78.0))
  nm.set(nm.LSR, deg2rad(28.0))
  nm.put()
  print "A4"

def playB4():
  nm.set(nm.LSP, deg2rad(26.0))
  nm.set(nm.LEP, deg2rad(-85.0))
  nm.set(nm.LSR, deg2rad(0.0))
  nm.put()
  print "B4"

def playC3():
  nm.set(nm.LSP, deg2rad(26.0))
  nm.set(nm.LEP, deg2rad(-90.0))
  nm.set(nm.LSR, deg2rad(0.0))
  nm.put()
  print "C3"

playC3()
nm.put()


def playD3():
  nm.set(nm.LSP, deg2rad(47.0))
  nm.set(nm.LEP, deg2rad(-65.0))
  nm.set(nm.LSR, deg2rad(32.0))
  nm.put()
  print "D3"





def playC6():
  nm.set(nm.RSP, deg2rad(47.0))
  nm.set(nm.REP, deg2rad(-67.0))
  nm.set(nm.RSR, deg2rad(-32.0))
  print "C6"


def playPose():
  nm.set(nm.LSR, deg2rad(-45.0))
  nm.set(nm.RSR, deg2rad(45.0))
  nm.set(nm.REP, deg2rad(-45.0))
  nm.set(nm.LEP, deg2rad(-45.0))
  nm.set(nm.RSP, deg2rad(-45.0))
  nm.set(nm.LSP, deg2rad(-45.0))
  nm.put()

def positionAdjustment():
  playF3()
  playC6()

def doBeat(hand):
  if(hand == "L"):
    da = deg2rad(2.0)
    nm.set(nm.LSP, nm.state[LSP,] + da)
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
#rospy.Subscriber("play_note", String, callback)
print "ready"
#home()
#nm.put()
#playC6()
#playG3()
#nm.put()



#positionAdjustment()
#nm.put()
#playPose()

#zero()
#nm.put()
time.sleep(3.0)
#doBeat("L")
#doBeat("R")
#doBeat("B")
rospy.spin()
#  cur,sub,maxBeat = nm.beat()

#zero()
#nm.put()

#nm.home()
#nm.put()
