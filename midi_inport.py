#!/usr/bin/env python

PORT=u'SAMSUNG_Android:SAMSUNG_Android MIDI 1 20:0'

# 64: E4

NOTES = []

def append_num(i):
    NOTES.append("C%d" % i)
    NOTES.append("C#%d" % i)
    NOTES.append("D%d" % i)
    NOTES.append("D#%d" % i)
    NOTES.append("E%d" % i)
    NOTES.append("F%d" % i)
    NOTES.append("F#%d" % i)
    NOTES.append("G%d" % i)
    NOTES.append("G#%d" % i)
    NOTES.append("A%d" % i)
    NOTES.append("A#%d" % i)
    NOTES.append("B%d" % i)

append_num(0)
for i in range(0,8):
    append_num(i)

import mido
import rospy
from std_msgs.msg import String

# print(dir(mido.messages))
#print mido.get_input_names()

def msg_str(msg):
    if msg.type == 'note_on':
        return NOTES[msg.note]
    else:
        return None;

def talker():
    pub = rospy.Publisher('play_note', String, queue_size=10)
    rospy.init_node('midi_inport', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    with mido.open_input(PORT) as inport:
        #print inport
        for msg in inport:
            #if rospy.is_shutdown(): # TODO: might hang till a note is pressed
                #break
            s = msg_str(msg)
            if s is not None:
                print s
                pub.publish(s)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
