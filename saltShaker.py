import narrative_machine_tmp as nm
import time

nm.init()
nm.vel(0,100)
nm.home()
nm.put()
def goToSaltRestPos():
  nm.set(3,-3.14/4.0)
  nm.set(5,0.0)
  nm.put()

def openSaltShaker():
  #nm.set(4,3.14/4.0)
  nm.set(6,0.0)
  nm.put()

def goToSaltShakePos():
  nm.set(3,1.73)
  nm.set(5,0.0)
  nm.put()

def saltShake():
 sc = 0
 while(sc < 5):
  nm.set(5,-3.14/15.0)
  nm.set(1,3.14/30.0)
  nm.set(3,2.0)
  nm.put()
  time.sleep(0.2)
  nm.set(5,3.14/15.0)
  nm.set(1,-3.14/30.0)
  nm.set(3,1.4)
  nm.put()
  time.sleep(0.2)
  sc = sc + 1
 nm.set(1,0.0)
 nm.put()

count = 0
time.sleep(2.0)
goToSaltRestPos()
time.sleep(2.0)
#openSaltShaker()
goToSaltShakePos()
time.sleep(2.0)
saltShake()
time.sleep(2.0)
goToSaltRestPos()
time.sleep(2.0)
nm.home()
nm.put()
