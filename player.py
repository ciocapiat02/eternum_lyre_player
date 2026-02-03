import mido

note_keys_map = {
    "67": "q",
    "69": "w",
    "71": "e",
    "72": "r",
    "74": "t",
    "76": "y",
    "78": "u",
    "79": "i",
    "81": "o",
}

midifile = mido.MidiFile("test.mid")

for msg in midifile.play():
    try:
        if msg.type == "note_on":
            print(note_keys_map[str(msg.note)])
    except Exception as e:
        pass
