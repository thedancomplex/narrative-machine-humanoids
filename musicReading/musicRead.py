import rospy
from std_msgs.msg import String

import mido
from mido import MidiFile, second2tick, tick2second

from time import sleep

midi_ticks_per_beat = -1
midi_tempo = 500000 #default tempo
true_tempo = 250000 # microseconds per beat

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

def parse_note(msg, pub):

    print("note value: {}".format(NOTES[msg['note']]))
    pub.publish(NOTES[msg['note']])

    sleep_time = msg['time']*true_tempo/midi_tempo
    
    print("sleeping for: {}".format(sleep_time))
    sleep(sleep_time)

def parse_tempo(msg, _output):
    print("setting tempo to: {}".format(msg['tempo']))

    midi_tempo = msg['tempo']


KNOWN_TYPES = {'note_on':parse_note, 'set_temp':parse_tempo}
    

def sendSong():
    f = MidiFile('hot_cross_buns.mid')
    midi_ticks_per_beat = f.ticks_per_beat
    pub = rospy.Publisher('musicSender', String, queue_size=10)
    rospy.init_node('robots', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for msg in f:
        dict_msg = msg.dict()
        if 'type' not in dict_msg:
            continue

        if not dict_msg['type'] in KNOWN_TYPES:
            continue

        KNOWN_TYPES[dict_msg['type']](dict_msg, pub)


if __name__ == '__main__':
    try:
        sendSong()
    except rospy.ROSInterruptException:
        pass
		   
