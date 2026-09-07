# music-utilities

Some scripts used music21. Use setup.sh for setup.

All exercises create the midi-file and ly-file (with pdf output). To create wav-file use fluidsynth.

General usage of any exercises:
```sh
python exs/ex1.py
fluidsynth soundfonts/SalamanderGrandPiano-V3.sf2 tmp/exercise.mid -F tmp/exercise.wav
ffplay -loop 0 tmp/exercise.wav
```

You can read the documentation of all exercises in exs/ itself.
