import rospy
import sys
from std_msgs.msg import String

import mido
from mido import MidiFile, second2tick, tick2second

from time import sleep

MIDI_TICKS_PER_BEAT = -1
MIDI_TEMPO = 500000 #default tempo
TRUE_TEMPO = 250000 # microseconds per beat

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

def parse_note(msg, pub, sleep_acc):
    print(msg)
    print("note value: {}".format(NOTES[msg['note']]))
    pub.publish(NOTES[msg['note']])

    # sleep time is in seconds, but we might have a different tempo
    sleep_time = sleep_acc*TRUE_TEMPO/MIDI_TEMPO
    
    print("sleeping for: {}".format(sleep_time))
    sleep(sleep_time)

def parse_tempo(msg):
    print("setting tempo to: {}".format(msg['tempo']))

    MIDI_TEMPO = msg['tempo']
    

def sendSong(song):
    f = MidiFile(song)
    MIDI_TICKS_PER_BEAT = f.ticks_per_beat
    pub = rospy.Publisher('musicSender', String, queue_size=10)
    rospy.init_node('robots', anonymous=True)

    sleep_acc = 0
    for msg in f:
        dict_msg = msg.dict()
        print(dict_msg)
        if 'type' not in dict_msg:
            continue

        sleep_acc += dict_msg['time']
        if dict_msg['type'] == 'note_on':
            parse_note(dict_msg, pub, sleep_acc)
            sleep_acc = 0
        elif dict_msg['type'] == 'parse_tempo':
            parse_temp(dict_msg)


if __name__ == '__main__':
    f = sys.argv[1]
    pbm = sys.argv[2]
    TRUE_TEMPO = float(pbm)/60*1000000
    try:
        sendSong(f)
    except rospy.ROSInterruptException:
        pass
		   
