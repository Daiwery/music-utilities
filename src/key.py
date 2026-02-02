"""Some utils for keys."""
import music21
import random


def generate_random_major_key() -> music21.key.Key:
    """Generate a random major key.

    Returns
    -------
    music21.key.Key
        The resulting major key.

    Examples
    --------
    >>> generate_random_key()
    C major
    """
    key = music21.note.Note(random.randint(0, 11)).name
    key = music21.key.Key(key)
    return key
