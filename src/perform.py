from music21.stream import Stream


def perform(stream: Stream):
    """Perform the music.

    This function just create midi-file and ly-file (with pdf output) for given Stream.
    """
    stream.write("mid", "tmp/exercise.mid")
    stream.write("lily.pdf", "tmp/exercise.ly")