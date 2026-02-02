"""
Key: C major
Progression: tonic degree -- 3 random degrees in random order without repeating (4 notes in total)
Stream: tonic triad -- progression repeated 4 times
"""
from src import *
from perform import *
from key import *
import random

# Define the key. It's C major always.
key = music21.key.Key("C")
# Get all pitches from given key.
pitches = key.pitches

# First pitch is tonic.
tonic = pitches[0]
# Also form the tonic triad as RomanNumeral.
tonicTriad = music21.roman.RomanNumeral("I", key)

# Create the stream.
stream = music21.stream.Stream()

# Create the tonic triad as chord.
tonicChord = music21.chord.Chord(list(tonicTriad.pitches)).closedPosition(forceOctave=3)
tonicChord.duration = music21.duration.Duration(type="half")
# Add the tonic chord in the start.
stream.append(tonicChord)

# Form the progression. It's just N first degrees in random order without repeating.
N = 4
progression = pitches[1:N+1]
random.shuffle(progression)
# Cut the progression. It's necessary 3 pitches.
progression = progression[:3]
# With tonic pitch progression has 4 pitches.
progression = [tonic] + progression[:3]
# Repeat 4 times.
progression *= 4

# Add all pitch in the stream.
for pitch in progression:
    # Define the octave.
    pitch.octave = 3
    # Form a note.
    note = music21.note.Note(pitch, type="half")
    stream.append(note)

perform(stream)
