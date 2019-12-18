import rospy
import sys
from std_msgs.msg import String

import mido
from mido import MidiFile, second2tick, tick2second, bpm2tempo

from time import sleep

MIDI_TICKS_PER_BEAT = -1
MIDI_TEMPO = 500000 #default tempo

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
    print(msg)
    print("note value: {}".format(NOTES[msg['note']]))
    pub.publish(NOTES[msg['note']])



def parse_tempo(msg):
    print("setting tempo to: {}".format(msg['tempo']))

    MIDI_TEMPO = msg['tempo']


def sendSong(song, tempo):
    f = MidiFile(song)
    MIDI_TICKS_PER_BEAT = f.ticks_per_beat
    pub = rospy.Publisher('play_note', String, queue_size=10)
    rospy.init_node('robots', anonymous=True)

    for msg in f:
        dict_msg = msg.dict()
        print(dict_msg)
        if 'type' not in dict_msg:
            continue

        if dict_msg['type'] == 'note_on':
            parse_note(dict_msg, pub)
        elif dict_msg['type'] == 'parse_tempo':
            parse_temp(dict_msg)

        # sleep time is in seconds, but we might have a different tempo
        sleep_time = dict_msg['time']*tempo/MIDI_TEMPO

        print("sleeping for: {}".format(sleep_time))
        sleep(sleep_time)


if __name__ == '__main__':
    f = sys.argv[1]
    pbm = sys.argv[2]
    tempo = bpm2tempo(float(pbm))
    try:
        sendSong(f, tempo)
    except rospy.ROSInterruptException:
        pass
