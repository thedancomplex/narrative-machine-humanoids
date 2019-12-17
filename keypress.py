import getch as g
import rospy
from std_msgs.msg import String
pub = rospy.Publisher('play_note', String, queue_size=10)
rospy.init_node('talker', anonymous=True)



while True:
  c = g.getch()
  if   c == 'z':
    pub.publish( 'C4' )
  elif c == 'x':
    pub.publish( 'D4' )
  elif c == 'c':
    pub.publish( 'E4' )
  elif c == 'v':
    pub.publish( 'F4' )
  elif c == 'b':
    pub.publish( 'A5' )
  elif c == 'n':
    pub.publish( 'B5' )
  elif c == 'm':
    pub.publish( 'C5' )
  elif c == ',':
    pub.publish( 'D5' )
  elif c == '.':
    pub.publish( 'E5' )
  elif c == '/':
    pub.publish( 'F5' )
  elif c == 's':
    pub.publish( 'C#4' )
  elif c == 'd':
    pub.publish( 'Eb4' )
  elif c == 'g':
    pub.publish( 'F#4' )
  elif c == 'h':
    pub.publish( 'Ab5' )
  elif c == 'j':
    pub.publish( 'Bb5' )
  elif c == 'l':
    pub.publish( 'C#5' )
  elif c == ';':
    pub.publish( 'Eb5' )
  print c
