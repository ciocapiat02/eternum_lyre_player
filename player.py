import mido

midifile = mido.MidiFile("test.mid")
for msg in midifile.play():
    try:
        print(msg.type)
        print(msg.note)
        print(msg.velocity)
    except Exception as e:
        pass
