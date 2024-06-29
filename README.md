# music-utilities

Some scripts used music21 and mingus.

### gen-progression.py
Generate a random progression. Save two files: txt-file and mid-file.

Usage:
```sh
python src/gen-progression.py
fluidsynth soundfonts/name.sf2 progression.mid -F progression.wav
open progression.wav
```

For more info see 'help'.
