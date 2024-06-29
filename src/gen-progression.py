import music21
import argparse
import core
import mingus.core.chords
import copy

parser = argparse.ArgumentParser(description="""
Generate a random progression of the given length on the given key.
""")
parser.add_argument(
    "-key", type=str, default="random",
    help="The key. Default 'random'."
)
parser.add_argument(
    "-length", type=int, default="4",
    help="The length of the progression. Must be 1 <= length <= 6. Default '4'."
)
parser.add_argument(
    "-mode", choices=["1", "2"], default="1",
    help="Various modes. Try it. Default '1'."
)
args = parser.parse_args()

if args.key == "random":
    key = core.generate_random_key()
else:
    key = music21.key.Key(args.key)

progression = core.generate_random_progression(key, args.length)

# txt-file with progression.
file = open("progression.txt", "w")
file.write(f"{key}\n")
file.write(" - ".join([numeral.figure for numeral in progression]))
file.write("\n")
for numeral in progression:
    pitches = list(map(lambda pitch: pitch.name.replace("-", "b"), numeral.pitches))
    chord = mingus.core.chords.determine(pitches)[0]
    file.write(f"{numeral.figure} : {chord}\n")

# Create stream with notes.
if args.mode == "1":
    stream = music21.stream.Stream()
    for numeral in progression:
        pitches = list(numeral.pitches)

        for i in range(len(pitches)):
            pitches[i].octave = 4
        
        tonic = copy.deepcopy(numeral.root())
        tonic.octave = 3
        pitches.append(tonic)
        
        chord = music21.chord.Chord(pitches)
        chord.duration = music21.duration.Duration(4)
        for i in range(1):
            stream.append(copy.deepcopy(chord))

if args.mode == "2":
    stream = music21.stream.Stream()
    for numeral in progression:
        sub_stream = music21.stream.Stream()

        pitches = list(numeral.pitches)
        length = len(pitches)

        for i in range(length):
            pitches[i].octave = 4

        tonic = copy.deepcopy(numeral.root())
        tonic.octave = 3

        border = music21.pitch.Pitch("F3")
        if tonic > border:
            tonic.octave = 2

        tonic = music21.note.Note(tonic)
        tonic.duration = music21.duration.Duration(length+1)
        sub_stream.append(tonic)

        for i, pitch in enumerate(pitches):
            note = music21.note.Note(pitch)
            note.duration = music21.duration.Duration(length-i)
            sub_stream.insertAndShift(i+1, note)
        
        stream.append(sub_stream)

# Repeat.
main_stream = music21.stream.Stream()
for i in range(4):
    main_stream.append(copy.deepcopy(stream))

# Save.
main_stream.write("mid", "progression.mid")
