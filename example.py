import narrative_machine_tmp as nm
import time
import sys
import socket
import select

UDP_IP = "192.168.8.212"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

sock.setblocking(0)

ready = select.select([mysocket], [], [], timeout_in_seconds)
if ready[0]:
  data = sock.recv(4096)

nm.init()

nm.vel(0,1023)

nm.home()
nm.put()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#charGetter = _GetchUnix()
#charGetter.__init__()

count = 0
while(count < 16):
  
  cur,sub,maxBeat = nm.beat()
  if(cur == 1):
    nm.set(5,-3.14/4.0)
  elif(cur == 2):
    nm.set(6,3.14/4.0)
  elif(cur == 3):
    nm.set(1, 3.14/4.0)
  elif(cur == 4):
    nm.set(2,3.14/4.0)
  nm.put()
  time.sleep(0.5)
  nm.home()
  nm.put()
  count += 1
nm.home()
nm.put()
#nm.nmexit()
