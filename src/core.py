"""
File with basic functions.
"""
import music21
import random
import mingus
from typing import List
import mingus.core.chords
import mingus.core.progressions


def generate_random_key() -> music21.key.Key:
    """Generate a random key.

    Returns
    -------
    music21.key.Key
        The resulting key.

    Examples
    --------
    >>> generate_random_key()
    g minor
    """
    key = music21.note.Note(random.randint(0, 11)).name
    key = music21.key.Key(key)
    key.mode = "major" if random.random() >= 0.5 else "minor"
    return key


def numerals_in_key(key: music21.key.Key) -> List[music21.roman.RomanNumeral]:
    """Return possible roman numerals in the given key.

    Parameters
    ----------
    key : music21.key.Key
        The key.

    Returns
    -------
    List[music21.roman.RomanNumeral]
        Possible roman numerals.

    Examples
    --------
    >>> numerals_in_key(music21.key.Key("C"))
    [
        <music21.roman.RomanNumeral I in C major>,
        <music21.roman.RomanNumeral ii in C major>,
        <music21.roman.RomanNumeral iii in C major>,
        <music21.roman.RomanNumeral IV in C major>,
        <music21.roman.RomanNumeral V in C major>,
        <music21.roman.RomanNumeral vi in C major>,
        <music21.roman.RomanNumeral viio in C major>
    ]

    >>> numerals_in_key(music21.key.Key("Am"))
    [
        <music21.roman.RomanNumeral i in a minor>,
        <music21.roman.RomanNumeral iio in a minor>,
        <music21.roman.RomanNumeral III in a minor>,
        <music21.roman.RomanNumeral iv in a minor>,
        <music21.roman.RomanNumeral v in a minor>,
        <music21.roman.RomanNumeral bVI in a minor>,
        <music21.roman.RomanNumeral bVII in a minor>
    ]
    """
    pitches = key.pitches[:-1]
    length = len(pitches)

    pitches += [music21.pitch.Pitch(f"{pitch.name}{pitch.octave+1}") for pitch in pitches]

    numerals = []
    for step in range(length):
        numerals.append(
            music21.roman.romanNumeralFromChord(
                music21.chord.Chord([
                    pitches[step], 
                    pitches[step+2], 
                    pitches[step+4]
                ]),
                key
            )
        )
    return numerals


def generate_random_progression(key: music21.key.Key, length: int) -> List[music21.roman.RomanNumeral]:
    """Generate a random progression on the given key.

    The resulting progression is not absolutely random. 
    Progression consists of chords built on the given key. 

    Progression always starts with a tonic chord.

    Parameters
    ----------
    key : music21.key.Key
        The major or minor key.

    length : int
        The length of the resulting chords. Length must be 1 <= length <= 6.

    Returns
    -------
    List[music21.roman.RomanNumeral]
        The resulting progression of the given length on the given key.

    Raises
    ------
    ValueError
        If the given key is not major or minor.

    Examples
    --------
    >>> generate_random_progression(music21.key.Key("C"), 4)
    [
        <music21.roman.RomanNumeral I in C major>, 
        <music21.roman.RomanNumeral iii in C major>, 
        <music21.roman.RomanNumeral IV in C major>, 
        <music21.roman.RomanNumeral viio in C major>
    ]
    >>> generate_random_progression(music21.key.Key("c"), 4)
    [
        <music21.roman.RomanNumeral i in c minor>, 
        <music21.roman.RomanNumeral iv in c minor>, 
        <music21.roman.RomanNumeral v in c minor>, 
        <music21.roman.RomanNumeral III in c minor>
    ]

    See Also
    --------
    get_all_numerals_in_key : Possible roman numerals.
    """
    numerals = numerals_in_key(key)
    tonic = numerals[0]
    progression = numerals[1:]

    random.shuffle(progression)
    progression = progression[:length-1]
    return [tonic] + progression
