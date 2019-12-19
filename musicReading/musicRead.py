import rospy
from std_msgs.msg import String

import sys
import argparse
from time import sleep

import mido
from mido import MidiFile, second2tick, tick2second, bpm2tempo



MIDI_TICKS_PER_BEAT = -1
MIDI_TEMPO = 500000 #default tempo

NOTES = []

def parse_args(args):
    x = argparse.ArgumentParser(
        "Sends a song note by note over the play_note ROS topic.\nTiming is done as the note should be played in the song.\n")

    x.add_argument(
        "song",
        nargs=1,
        help="The path to a midi file to be played")
    x.add_argument(
        "bpm",
        nargs='?',
        type=float,
        help="A custom tempo (in bpm) to set")
    x.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=rospy.INFO)
    x.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=rospy.DEBUG)
    return x.parse_args(args)


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
    rospy.loginfo("note value: {}".format(NOTES[msg['note']]))
    pub.publish(NOTES[msg['note']])



def parse_tempo(msg):
    rospy.loginfo("setting tempo to: {}".format(msg['tempo']))

    MIDI_TEMPO = msg['tempo']

def process_message(msg, pub):
    dict_msg = msg.dict()

    rospy.logdebug("{}".format(dict_msg))
    if 'time' not in dict_msg:
        return 0

    if dict_msg['type'] == 'note_on':
        parse_note(dict_msg, pub)
    elif dict_msg['type'] == 'parse_tempo':
        parse_temp(dict_msg)
    return 1


def sendSongTempo(song, tempo):
    rospy.loginfo("Playing {} with custom tempo: {}".format(song, tempo))
    f = MidiFile(song)
    MIDI_TICKS_PER_BEAT = f.ticks_per_beat


    for msg in f.play():
        dict_msg = msg.dict()
        if (process_message(msg, pub)):
            # sleep time is in seconds, but we might have a different tempo
            sleep_time = dict_msg['time']*tempo/MIDI_TEMPO

            rospy.logdebug("sleeping for {}.".format(sleep_time))
            sleep(sleep_time)

def sendSong(song, pub):
    rospy.loginfo("Playing {} with their tempo".format(song))
    f = MidiFile(song)

    for msg in f.play():
        process_message(msg, pub)



if __name__ == '__main__':
    a = parse_args(sys.argv[1:])
    f = a.song[0]
    pub = rospy.Publisher('play_note', String, queue_size=10)

    rospy.init_node('robots', anonymous=True, log_level=a.loglevel)

    try:
        if a.bpm is not None:
            sendSongTempo(f, bpm2tempo(a.pbm), pub)
        else:
            sendSong(f, pub)
    except rospy.ROSInterruptException:
        pass
