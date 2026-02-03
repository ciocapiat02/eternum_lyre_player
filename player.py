import mido

midifile = mido.MidiFile("test.mid")
for msg in midifile.play():
    print(msg)
