import narrative_machine_tmp as nm
import time
import random as r
import rospy
from std_msgs.msg import String
#pub = rospy.Publisher('play_note', String, queue_size=10)
#rospy.init_node('talker', anonymous=True)

joint = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
RSP = 1
LSP = 2
REP = 5
LEP = 6


nm.init()

nm.vel(0,100)
nm.home()
nm.put()
time.sleep(1.0)
nm.set(6,-3.14/9.0)
nm.set(5,3.14/9.0)
nm.set(11,-.2)
nm.set(12,.2)
nm.put()
time.sleep(0.5)
nm.set(1,-3.14/6.0)
nm.set(2,3.14/6.0)
nm.put()
i=0

ts = 0.1

def home():
  nm.set(1,-3.14/6.0)
  nm.set(2,3.14/6.0)
  nm.set(5,3.14/9.0)
  nm.set(6,-3.14/9.0)
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
  joint[RSP] = -3.14/6.0
  nm.set(RSP,joint[RSP])
  nm.set(REP,-3.14/9.0)
  print "C2"
def playF3():
  global joint
  joint[LSP] = 3.14/6.0-0.03
  nm.set(LSP,joint[LSP])
  nm.set(LEP,3.14/9.0)
def doBeat(hand):
  if(hand == "L"):
    da = 0.1
    nm.set(LSP, joint[LSP] + da)
    nm.put()
    time.sleep(1.0)
    nm.set(LSP, joint[LSP])
    nm.put()
home()
#while(True):
rospy.init_node('listener', anonymous=True)
rospy.Subscriber("play_note", String, callback)
print "ready"
playC5()
playF3()
nm.put()
time.sleep(5.0)
doBeat("L")
rospy.spin()
#  cur,sub,maxBeat = nm.beat()




nm.home()
nm.put()
