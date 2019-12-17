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
nm.set(1,-3.14/4.0)
nm.set(2,3.14/4.0)
nm.put()
i=0

drumState = 1
drumStateL = 1
drumStateR = 1

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

def doDrumL():
  global drumStateL
  if(drumStateL == 1):
    nm.set(1,-3.14/6.0)
    drumStateL = 0
  else:
    nm.set(1,-3.14/4.0)

def doDrumR():
  global drumStateR
  if(drumStateR == 1):
    nm.set(2,3.14/6.0)
    drumStateR = 0
  else:
    nm.set(2,3.14/4.0)

while(True):
 cur,sub,maxBeat = nm.beat()
 if (i < 0):
   i += 1
   doDrum()
   nm.put()

 else:
  if(sub == 1):
    drumStateR = 1
  if(sub == 3):
    drumStateR = 1
    drumStateL = 1
#  if(cur == 1  and sub==1):
#    drumStateR = 1
#  if(cur == 2 and sub == 1):
#  if(cur == 3 and sub == 1):
#    drumStateR = 1
#    drumStateL = 1
  #if(cur == 4 and sub == 1):
  doDrumR()
  doDrumL()  
  nm.put()

nm.home()
nm.put()
