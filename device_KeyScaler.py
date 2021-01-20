# name=BigSmilez Key Scaler
# FL Studio script to make the white keys on a MIDI keyboard play the scale of your choice!
# Author: Preet Kamal Singh Minhas, MARCHINGBYTES TECHNOLOGY SOLUTIONS PRIVATE LIMITED
# https://marchingbytes.com
# License: MIT
# If you like this script, please follow me on IG, SoundCloud, Beatstars @bigsmilezmusic
# https://instagram.com/bigsmilezmusic
# https://soundcloud.com/bigsmilezmusic
# https://www.beatstars.com/bigsmilezmusic/feed

# CONSTANTS, DO NOT CHANGE
# Root notes
C = 0
C_SHARP = 1
D = 2
D_SHARP = 3
E = 4
F = 5
F_SHARP = 6
G = 7
G_SHARP = 8
A = 9
A_SHARP = 10
B = 11

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
WHITE_KEYS = [0,2,4,5,7,9,11]
MIDI_NOTE_ON = 144
MIDI_NOTE_OFF = 128
# END OF CONSTANT DEFINITIONS

# Scale definitions
MAJOR = [0, 2, 4, 5, 7, 9, 11, 12]
MINOR_NATURAL = [0, 2, 3, 5, 7, 8, 10, 12]
# add more scale definitions here to enhance the capabilities of this script.
# Ensure that the array has 7 entries (all white keys C-B must be mapped for this script to work correctly)


# -- MAKE SCALE/ROOT NOTE CHANGES HERE --
# Change these two values to play the scale you desire (choose from the variables defined above)
ROOT_NOTE = D_SHARP
SCALE = MINOR_NATURAL

# If you don't know python, do not make changes to the code that follows

print("Selected root note:", NOTE_NAMES[ROOT_NOTE])
if SCALE == MINOR_NATURAL:
    print("Minor Natural scale")
elif SCALE == MAJOR:
    print("Major scale")

# FL event capture
def OnMidiMsg(event):
    if event.midiId == MIDI_NOTE_ON or event.midiId == MIDI_NOTE_OFF:
        # event.data1 contains the note value, starting at 0 for lowest C
        print("Note detected", event.midiId, event.data1, event.data2)
        offset_from_c = event.data1 % 12
        octave = int(event.data1 / 12)
        key_index = __white_key_index__(offset_from_c)
        if key_index == -1:
            # black key pressed, do nothing
            return
        print(key_index, octave)
        new_event_value = ROOT_NOTE + SCALE[key_index] + 12*octave
        print(new_event_value)
        event.data1 = new_event_value


def __white_key_index__(key_number):
    """Returns the index of key if it is a white key, -1 in case of black key"""
    try:
        index = WHITE_KEYS.index(key_number)
        return index
    except ValueError:
        return -1
