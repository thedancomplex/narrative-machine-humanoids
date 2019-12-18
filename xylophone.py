import narrative_machine_tmp as nm
import time
import random as r
import rospy
import numpy as np
from std_msgs.msg import String
#pub = rospy.Publisher('play_note', String, queue_size=10)
#rospy.init_node('talker', anonymous=True)

nm.init()

nm.vel(0,1000)

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

def start():
  nm.set(nm.LSP, deg2rad(22.0))
  nm.set(nm.LEP, deg2rad(-91.0))
  nm.set(nm.LSR, deg2rad(0.0))
  print "start pose L"
  nm.set(nm.RSP, deg2rad(22.0))
  nm.set(nm.REP, deg2rad(-96.0))
  nm.set(nm.RSR, deg2rad(0.0))
  print "start pose R"
  nm.put()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    if(data.data == "F3"):
      playF3()
    elif(data.data == "G3"):
      playG3()
    elif(data.data == "A3"):
      playA3()
    elif(data.data == "B3"):
      playB3()
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
    elif(data.data == "A4"):
      playA4()
    elif(data.data == "B4"):
      playB4()
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
    elif(data.data == "A5"):
      playA5()
    elif(data.data == "B5"):
      playB5()
    elif(data.data == "C6"):
      playC6()
    nm.put()
    doBeat("B")
    start()

############ L hand lower

def playF3():
  nm.set(nm.LEP, deg2rad(-30.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.LSR, deg2rad(32.0))
  nm.put()
  time.sleep(0.05)
  nm.set(nm.LSP, deg2rad(47.0))
  nm.set(nm.LEP, deg2rad(-65.0))
  print "F3"

def playG3():
  '''
  nm.set(nm.LEP, deg2rad(-30.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.LSR, deg2rad(32.0))
  nm.put()
  time.sleep(0.05)
  nm.set(nm.LSP, deg2rad(44.0))
  nm.set(nm.LEP, deg2rad(-69.0))
  nm.put()
  time.sleep(0.05)
  '''
  nm.set(nm.LEP, deg2rad(-75.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.LSP, deg2rad(27.0))
  nm.set(nm.LSR, deg2rad(0.0))


  print "G3"

def playA3():
  '''
  nm.set(nm.LEP, deg2rad(-30.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.LSR, deg2rad(28.0))
  nm.put()
  time.sleep(0.05)
  nm.set(nm.LEP, deg2rad(-78.0))
  nm.put()
  time.sleep(0.05)
  nm.set(nm.LSP, deg2rad(38.0))
  '''
  nm.set(nm.LEP, deg2rad(-80.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.LSP, deg2rad(27.0))
  nm.set(nm.LSR, deg2rad(0.0))

  print "A3"

def playB3():
  nm.set(nm.LEP, deg2rad(-85.0))
  nm.put()
  time.sleep(0.02)
  nm.set(nm.LSP, deg2rad(26.0))
  nm.set(nm.LSR, deg2rad(0.0))
  print "B3"

def playC4():
  nm.set(nm.LSP, deg2rad(26.0))
  nm.set(nm.LEP, deg2rad(-91.0))
  nm.set(nm.LSR, deg2rad(0.0))
  print "C4"

def playD4():
  nm.set(nm.LSP, deg2rad(27.0))
  nm.set(nm.LEP, deg2rad(-95.0))
  nm.set(nm.LSR, deg2rad(0.0))
  print "D4"

def playE4():
  nm.set(nm.LEP, deg2rad(-100.0))
  nm.put()
  time.sleep(0.02)
  nm.set(nm.LSP, deg2rad(28.0))
  nm.set(nm.LSR, deg2rad(0.0))
  print "E4"

def playF4():
  nm.set(nm.LEP, deg2rad(-104.5))
  nm.put()
  time.sleep(0.02)
  nm.set(nm.LSP, deg2rad(29.0))
  nm.set(nm.LSR, deg2rad(0.0))
  print "F4"

def playG4():
  nm.set(nm.LEP, deg2rad(-109.5))
  nm.put()
  time.sleep(0.05)
  nm.set(nm.LSP, deg2rad(30.0))
  nm.set(nm.LSR, deg2rad(-5.0))
  print "G4"

def playA4():
  nm.set(nm.LEP, deg2rad(-114.5))
  nm.put()
  time.sleep(0.07)
  nm.set(nm.LSP, deg2rad(32.0))
  nm.set(nm.LSR, deg2rad(-7.0))
  print "A4"

################ R hand Lower

def playB4():
  nm.set(nm.REP, deg2rad(-110.0))
  nm.put()
  time.sleep(0.07)
  nm.set(nm.RSP, deg2rad(31.0))
  nm.set(nm.RSR, deg2rad(-5.0))
  print "B4"

def playC5():
  nm.set(nm.REP, deg2rad(-105.0))
  nm.put()
  time.sleep(0.05)
  nm.set(nm.RSP, deg2rad(30.0))
  nm.set(nm.RSR, deg2rad(-15.0))
  print "C5"

def playD5():
  nm.set(nm.RSP, deg2rad(30.0))
  nm.set(nm.REP, deg2rad(-100.0))
  nm.set(nm.RSR, deg2rad(-15.0))
  print "D5"

def playE5():
  nm.set(nm.RSP, deg2rad(36.0))
  nm.set(nm.REP, deg2rad(-96.0))
  nm.set(nm.RSR, deg2rad(-15.0))
  print "E5"

def playF5():
  nm.set(nm.RSP, deg2rad(35.0))
  nm.set(nm.REP, deg2rad(-88.0))
  nm.set(nm.RSR, deg2rad(-39.0))
  print "F5"

def playG5():
  nm.set(nm.RSP, deg2rad(37.0))
  nm.set(nm.REP, deg2rad(-84.5))
  nm.set(nm.RSR, deg2rad(-35.0))
  print "G5"

def playA5():
  nm.set(nm.RSP, deg2rad(38.0))
  nm.set(nm.REP, deg2rad(-79.0))
  nm.set(nm.RSR, deg2rad(-26.0))
  print "A5"

def playB5():
  '''
  nm.set(nm.REP, deg2rad(-75.0))
  time.sleep(0.05)
  nm.set(nm.RSP, deg2rad(41.0))
  nm.set(nm.RSR, deg2rad(-28.0))
  '''
  nm.set(nm.REP, deg2rad(-77.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.RSP, deg2rad(30.0))
  nm.set(nm.RSR, deg2rad(0.0))
  print "B5"

def playC6():
  '''
  nm.set(nm.REP, deg2rad(-67.0))
  time.sleep(0.11)
  nm.set(nm.RSP, deg2rad(47.0))
  nm.set(nm.RSR, deg2rad(-32.0))
  '''
  nm.set(nm.REP, deg2rad(-72.0))
  nm.put()
  time.sleep(0.1)
  nm.set(nm.RSP, deg2rad(31.0))
  nm.set(nm.RSR, deg2rad(0.0))
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
  #time.sleep(1.0)
  a_LSP = nm.get(nm.LSP)
  a_RSP = nm.get(nm.RSP)
  da_L = deg2rad(2.0)
  da_R = deg2rad(2.5)
  #print a_LSP

  if(hand == "L"):
    nm.set(nm.LSP, a_LSP + da_L)
    nm.put()
  elif(hand == "R"):
    nm.set(nm.RSP, a_RSP - da_R)
    nm.put()
  elif(hand == "B"):
    nm.set(nm.LSP, a_LSP + da_L)
    nm.set(nm.RSP, a_RSP - da_R)
    nm.put()
  time.sleep(0.1)
  nm.set(nm.LSP, a_LSP)
  nm.set(nm.RSP, a_RSP)
  nm.put()
  time.sleep(0.05)


rospy.init_node('listener', anonymous=True)
rospy.Subscriber("play_note", String, callback)

start()
nm.put()


rospy.spin()


start()
nm.put()
