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
stream = music21.stream.Stream()
for numeral in progression:
    pitches = list(numeral.pitches)

    for i in range(len(pitches)):
        pitches[i].octave = 4
    
    tonic = copy.deepcopy(numeral.root())
    tonic.octave = 3
    pitches.append(tonic)
    
    chord = music21.chord.Chord(pitches)
    for i in range(4):
        stream.append(copy.deepcopy(chord))

# Repeat.
main_stream = music21.stream.Stream()
for i in range(4):
    main_stream.append(copy.deepcopy(stream))

# Save.
main_stream.write("mid", "progression.mid")
