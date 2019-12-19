import narrative_machine_tmp as nm
import time
nm.init()

nm.vel(0,1023)
nm.home()
nm.put()
time.sleep(1.0)
nm.set(6,-3.14/9.0)
nm.set(5,3.14/9.0)
nm.put()
time.sleep(0.5)
#nm.set(1,-3.14/4.0)
#nm.set(2,3.14/4.0)
#nm.put()
i=0

drumState = 1
drumState_2 = 1
leftDown = 0
rigthDown = 0
def leftHandDown():
  global leftDown
  nm.set(2,3.14/4.0)
  nm.put()
  leftDown = 1

def rigthHandDown():
  global rightDown
  nm.set(1,-3.14/4.0)
  nm.put()
  rightDown = 1

leftHandDown()

time.sleep(2.0)

rigthHandDown()

time.sleep(2.0) 
nm.set(2,-3.14/6.0)
nm.set(1,-3.14/6.0)
nm.put()
def doDrum():
  global drumState, drumState_2
  nm.set(2,-3.14/4.0)
  nm.set(1,-3.14/6.0)

while(True):
  cur,sub,maxBeat = nm.beat()
  if(cur == 1  and sub==1):
    doDrum()
  if(cur == 2 and sub == 1):
    doDrum()
  if(cur == 3 and sub == 1):
    doDrum()
  if(cur == 4 and sub == 1):
    doDrum()
  if(cur == 1 and sub == 3):
    doDrum()
  if(cur == 2 and sub == 3):
    doDrum()
  if(cur == 3 and sub == 3):
    doDrum()
  if(cur == 4 and sub == 3):
    doDrum()  
  nm.put()
  i += 1

nm.home()
nm.put()
