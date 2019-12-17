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

# print(dir(mido.messages))
# print mido.get_input_names()

with mido.open_input(PORT) as inport:
    print inport
    for msg in inport:
        print '--'
        if msg.type == 'note_on':
            print msg
            print "ON"
            print(msg.note)
            print(NOTES[msg.note])
