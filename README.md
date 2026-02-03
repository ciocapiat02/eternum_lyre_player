# Eternum lyre player
Basically i was intrigued by a post on the r/eternumites in which a gui plays something very cool with the lyre in eternum 0.9.
this is the post:
So i wanted to create a simple python script that will read a midi file and play it on the lyre.
The easiest way was to make the script read the midi file and simulate a keypress, since in the game every note is mapped to a key, so, here it is.

# Install
clone this repo and install the required dependencies

```bash
git clone https://github.com/ciocapiat02/eternum_lyre_player.git
pip install -r requirements.txt
```

## Linux on wayland 
Unfortunately, there is currently no library that works seamlessly with Wayland and virtual keyboards.
The workaround used here is the `ydotool` utility. If you're using Wayland, install the appropriate package for your distribution.
For example, on Fedora:

```bash
sudo dnf install ydotool
```

# Run
To run this script you'll need to first get or create a midi file.
Once you have it you have to run the `player.py` script passing the name or the path to the file as first argument

```bash
python3 player.py test.mid
```

Obviously the game will only play the notes present in the game files, so be aware that the only notes that can be played are:
g4, a4, b4, c5, d5, e5, f5, g5, a5
