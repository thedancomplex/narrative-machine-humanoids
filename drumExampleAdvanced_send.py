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

notes =["E",
        "E",
        "E",
        "E",
        "E",
        "E",
        "E",
        "G",
        "C",
        "D",
        "E",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",#begining part
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG",
        "CG",
        "CG",
        "CG",
        "FC",
        "DA",
        "GD",
        "GD",
        "CG"]# this note and above is verse


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
pub.publish(notes[note]+"1")
note = note + 1
tmp = raw_input()
pub.publish(notes[note]+"1")
note = note + 1
time.sleep(short)
pub.publish(notes[note]+"1")
note = note + 1
time.sleep(short)
pub.publish(notes[note]+"1")
time.sleep(longT)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(short)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(short)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(longT)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(short)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(short)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(0.75*longT)
note = note + 1
pub.publish(notes[note]+"1")
time.sleep(short)
note = note + 1



tmpNote = notes[note]
pub.publish(tmpNote[0]+"1")
#pub.publish("E1")
#pub.publish("E1")
#pub.publish("E1")

started = False
first_time = True
while(True):
 cur,sub,maxBeat = nm.beat()
 print(timeSwitch,count)
 tmpStr = notes[note]
 print(i)
 if(i >= 28 or started == True):
  if(started == False):  
    i = 0
    started = True
  if((cur == 2 or cur == 4)  and sub == 1):
    if(timeSwitch == 0):
      if(not first_time):
       hello_str = tmpStr[0] + "1"
       rospy.loginfo(hello_str)
       pub.publish(hello_str)
    elif(timeSwitch == 1):
      hello_str = "H1"
    # send C1
  elif((cur == 1 or cur == 3) and sub == 1):
    first_time = False
    if(timeSwitch == 0):
      hello_str = tmpStr[1] + "1"
    elif(timeSwitch == 1):
      hello_str = "E1"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    # send F1
  """if(cur == 2 and sub == 1):
    doDrum()
  if(cur == 3 and sub == 1):
    doDrum()
  if(cur == 4 and sub == 1):
    doDrum()"""
#  if(cur == 1 and sub == 3):
#    doDrum()
  
  #nm.put()
  if(count >=16):
    if(timeSwitch == 0):
        timeSwitch = 1
    elif(timeSwitch == 1):
        timeSwitch = 0
    count = 0
  count += 0
  if(i == 8):
    note += 1
    i = 0
 i+=1
#nm.home()
#nm.put()
