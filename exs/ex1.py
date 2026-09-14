"""
This excise is about random degrees in random order with/without repeating in given/random key.

Tonic triad and tonic degree are played first, then generated progression are played as half-note.

Change 'parameter' section for your pleasure.
"""
from src import *
from perform import *
from key import *
import random

# ===== Parameters =====
# key = random_major_key()
key = music21.key.Key("A")
forceOctave = 2

def generate_progression(pitches):
    """Function for generation progression via pitches (with tonic note) from given key."""
    tonic = pitches[0]
    delta = tonic.octave - forceOctave
    for pitch in pitches:
        pitch.octave -= delta

    progression = pitches[:5]
    random.shuffle(progression)
    return [tonic] + progression[:3]
    

pitches = key.pitches
for pitch in pitches:
    pitch.octave -= 1

tonic = pitches[0]
tonicTriad = music21.roman.RomanNumeral("I", key)

stream = music21.stream.Stream()

tonicChord = music21.chord.Chord(list(tonicTriad.pitches)).closedPosition(forceOctave=forceOctave)
tonicChord.duration = music21.duration.Duration(type="half")
stream.append(tonicChord)

progression = generate_progression(pitches)
progression *= 4

for pitch in progression:
    note = music21.note.Note(pitch, type="half")
    stream.append(note)

perform(stream)
