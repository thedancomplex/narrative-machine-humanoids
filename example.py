import narrative_machine_tmp as nm
import time

nm.init()

nm.vel(0,1023)

nm.home()
nm.put()

count = 0
while(count < 16):
  cur,sub,maxBeat = nm.beat()
  if(cur == 1):
    nm.set(5,-3.14/4.0)
  elif(cur == 2):
    nm.set(6,3.14/4.0)
  elif(cur == 3):
    nm.set(1,3.14/4.0)
  elif(cur ==4 ):
    nm.set(2,3.14/4.0)
  nm.put()
  time.sleep(0.5)
  nm.home()
  nm.put()
  count += 1
nm.home()
nm.put()
#nm.nmexit()
