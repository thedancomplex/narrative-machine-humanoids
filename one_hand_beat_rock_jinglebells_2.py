import narrative_machine_tmp as nm
import time
import random
import termios
import sys
import select
import tty
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
nm.set(2,-3.14/4.0)
nm.put()
i=0

mainDrumState = 1
secondDrumState = 1
p = 30 # 1-100 
r = 0
cp = '\x1b'
flag = 0
subp = 0
old_settings = termios.tcgetattr(sys.stdin)


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def doSecondDrum():
  global secondDrumState
  if(secondDrumState == 1):
    nm.set(1,-3.14/6.0)
    secondDrumState = 0
  else:
    nm.set(1,-3.14/2.0)
    secondDrumState = 1

def doMainDrum():
  global mainDrumState
  if(mainDrumState == 1):
    nm.set(2,3.14/2.0)
    mainDrumState = 0
  else:
    nm.set(2,3.14/6.0)
    mainDrumState = 1

try:
  tty.setcbreak(sys.stdin.fileno())

  while(True):
    cur,sub,maxBeat = nm.beat()
    if( (cur == 1 or cur == 3) and sub == 1):
      isData()
      c = sys.stdin.read(1)
      if (c == cp):
        flag = 1
        print(1)
      else:
        flag = 0
        print(0)
      cp = c

    if(sub == 1):
      doMainDrum()
    if(sub == 2):
      doMainDrum()
    if(sub == 3):
      doMainDrum()
    if(sub == 4):
      doMainDrum()


    if(sub == 1 and flag == 1):
      r = (random.uniform(1, 100) < p)
    else:
      r = 1

    if(r):
      if(sub != subp):
        doSecondDrum()
        subp = sub

    else:
      if(sub == 1):
        doSecondDrum()
      if(sub == 3):
        doSecondDrum()

    nm.put()
    i += 0


finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

nm.home()
nm.put()
