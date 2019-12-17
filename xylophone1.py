import narrative_machine_tmp as nm
import time
import random as r
nm.init()

nm.vel(0,1023)
nm.home()
nm.put()
time.sleep(1.0)
nm.set(6,-3.14/9.0)
nm.set(5,3.14/9.0)
nm.put()
time.sleep(0.5)
nm.set(1,-3.14/6.0)
nm.set(2,3.14/6.0)
nm.put()
i=0

ts = 0.1

def home():
  nm.set(1,-3.14/6.0)
  nm.set(2,3.14/6.0)
  nm.set(5,3.14/9.0)
  nm.set(6,-3.14/9.0)
  nm.put()

def playB():
  nm.set(5,3.14/9.0)
  nm.set(1,-3.14/3.9)

def playF():
  nm.set(6,-3.14/9.0)
  nm.set(2,3.14/4.1)

def playA():
  nm.set(5,3.14/7.0)
  nm.set(1,-3.14/3.8)

def playG():
  nm.set(6,-3.14/7.0)
  nm.set(2,3.14/4.0)

def playBF():
  nm.set(5,3.14/9.0)
  nm.set(6,-3.14/9.0)
  nm.set(1,-3.14/3.9)
  nm.set(2,3.14/4.1)

def playMixedBeat(beats):
  i=0
  while(i < beats):
    cur,sub,maxBeat = nm.beat()
    if(cur == 1 and sub == 1):
      playB()
    if(cur == 1 and sub == 3):
      playB()
      playF()
    if(cur == 2 and sub == 1):
      playF()
    if(cur == 2 and sub == 4):
      playG()
      playA()

    if(cur == 3 and sub == 2):
      playA()
    if(cur == 3 and sub == 3):
      playF()
    
    if(cur == 4 and sub == 2):
      playG()
    if(cur == 4 and sub == 4):
      playG()
      playB()

    nm.put()    
    time.sleep(ts)
    home() 
    i += 1

def playRandom(beats):
  i=0
  while(i < beats):
    cur,sub,maxBeat = nm.beat()
    if(round(r.random()) == 1):
      randVal1 = r.random()
      if(round(randVal1) == 0):
        randVal = r.randint(1,4)
        if(randVal == 1):
          playA()
        if(randVal == 2):
	  playF()
	if(randVal == 3):
	  playB()
	if(randVal == 4):
	  playG()
      if(round(randVal1) == 1):
	randVal = r.randint(1,4)
	if(randVal == 1):
	  playA()
	  playF()
	if(randVal == 2):
	  playA()
	  playG()
	if(randVal == 3):
	  playB()
	  playF()
	if(randVal == 4):
	  playB()
	  playG()

    nm.put()
    time.sleep(ts)
    home()
    i += 1

def playOnBeatFast(beats):
  i=0
  cur,sub,maxBeat = nm.beat()
  while(i < beats):
    if(cur == 1 and sub == 1):
      playB()
      playF()
    if(cur == 1 and sub == 3):
      playB()
    if(cur == 2 and sub == 1):
      playG() 
    if(cur == 2 and sub == 3):
      playG()
      playB()
    if(cur == 3 and sub == 1):
      playA()
    if(cur == 3 and sub == 3):
      playF()
      playA()
    if(cur == 4 and sub == 1):
      playG()
    if(cur == 4 and sub == 3):
      playG()

    nm.put()
    time.sleep(ts)
    home()
    i += 1

def playOnBeatSlow(beats):
  i=0
  while(i < beats):
    cur,sub,maxBeat = nm.beat()
    if(cur == 1 and sub == 1):
      playB()
      playF()
    if(cur == 2 and sub == 1):
      playG()
    if(cur == 3 and sub == 1):
      playA()
    if(cur == 4 and sub == 1):
      playG()
      playB()

    nm.put()
    time.sleep(ts)
    home()
    i += 1

def playCal(beats):
  i=0
  while(i < beats):
    cur,sub,maxBeat = nm.beat()
    if(cur == 1 and sub == 1):
      playBF()
    if(cur == 2 and sub == 1):
      playBF()
    if(cur == 3 and sub == 1):
      playBF()
    if(cur == 4 and sub == 1):
      playBF()

    nm.put()
    time.sleep(ts)
    home()
    i += 1

#playRandom(64)
#playOnBeatFast(64)
#playOnBeatSlow(64)

while(i < 300):
  cur,sub,maxBeat = nm.beat()
  if(maxBeat == 1 or maxBeat == 5):
    home()
  if(maxBeat == 0):
    playRandom(16) 
  if(maxBeat == 7):
    playOnBeatFast(16)
  if(maxBeat == 4 or maxBeat == 6 or maxBeat == 7):
    playOnBeatSlow(16)

nm.home()
nm.put()
