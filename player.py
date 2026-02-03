import mido
import sys
import time
from keyboardController import KeyboardController

note_keys_map = {
    "67": "q",
    "69": "w",
    "71": "e",
    "72": "r",
    "74": "t",
    "76": "y",
    "77": "u",
    "79": "i",
    "81": "o",
}

def play(filename):
    midifile = mido.MidiFile(filename)
    kb = KeyboardController()
    for msg in midifile.play():
        try:
            if msg.type == "note_on":
                kb.type(note_keys_map[str(msg.note)])
        except Exception as e:
            pass

try:
    filename = sys.argv[1]
except IndexError:
    print("you need to give me a midi file")
    exit()
    
print(f"will start to play {filename} in 10 seconds, switch to eternum and wait for it")
time.sleep(10)
play(filename)
