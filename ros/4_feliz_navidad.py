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

notes =[
        "D",
        "C",
        "F",
        "F"]#begining part


pub = rospy.Publisher('play_note', String, queue_size=10)
rospy.init_node('talker', anonymous=True)

"""
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
"""


timeSwitch = 0
count = 0
i=0
note = 0
short = 0.75
longT = 1.5
pub.publish("F1")
tmp = raw_input()
started = False
first_time = True
while(True):
 cur,sub,maxBeat = nm.beat()
 tmpStr = notes[note]
 if(i >= 28 or started == True):
  if(started == False):
    i = 0
    started = True  
  if((cur == 1)  and sub == 1):
       hello_str = tmpStr + "1"
       rospy.loginfo(hello_str)
       pub.publish(hello_str)
       note = note + 1
    # send C1
    # send F1
    #  if(cur == 1 and sub == 3):
    #    doDrum()
  
  #nm.put()
  if(note == 3):
   note = 0
 i+=1
#nm.home()
#nm.put()
