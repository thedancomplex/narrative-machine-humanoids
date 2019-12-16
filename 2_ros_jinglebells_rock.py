import narrative_machine_tmp as nm
import time
import rospy
from std_msgs.msg import String


nm.init()
"""

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
"""


pub = rospy.Publisher('play_note', String, queue_size=10)
rospy.init_node('talker', anonymous=True)

xflag = 0
while(True):
 cur,sub,maxBeat = nm.beat()
 if((cur == 1)  and sub == 1):
       hello_str = "X1"
       if (xflag == 0):
         hello_str = "X2"
         xflag = 1
       else:
         xflag = 0
       rospy.loginfo(hello_str)
       pub.publish(hello_str)
  
  #nm.put()
#nm.home()
#nm.put()
