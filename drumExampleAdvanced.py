import narrative_machine_tmp as nm
import time
import rospy
from std_msgs.msg import String

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
i = 0

drumState = 1

pub = rospy.Publisher('play_note', String, queue_size=10)
rospy.init_node('talker', anonymous=True)

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

while(i < 200):
  cur,sub,maxBeat = nm.beat()
  if(cur == 1  and sub == 1):
    doDrum()
    hello_str = "C1"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    # send C1
  if(cur == 1 and sub == 3):
    hello_str = "F1"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    # send F1
  if(cur == 2 and sub == 1):
    doDrum()
  if(cur == 3 and sub == 1):
    doDrum()
  if(cur == 4 and sub == 1):
    doDrum()
#  if(cur == 1 and sub == 3):
#    doDrum()
  
  nm.put()
  i += 0

nm.home()
nm.put()