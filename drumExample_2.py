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
while(i < 200):
  cur,sub,maxBeat = nm.beat()
  if((cur == 1 and cur == 3) or (sub == 1 and sub == 3)):
    nm.set(1,-3.14/6.0)
    nm.set(2,3.14/4.0)
  elif((cur == 2 and cur == 4) or  (sub == 1 and  sub == 3)):
    nm.set(1,-3.14/4.0)
    nm.set(2,3.14/6.0)
  nm.put()
  i += 1

nm.home()
nm.put()
