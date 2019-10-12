import narrative_machine_tmp as nm
import time
import sys

nm.init('server')
i=0
try:
 while(True):
  if(i > 78):
    print '.'
    i=0
  else:
    print '.',
  i += 1
  sys.stdout.flush()
  time.sleep(1.0)
except:
 nm.nmexit() 
