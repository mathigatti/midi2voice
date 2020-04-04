# Singing Synthesis from MIDI file

This script relies on the [sinsy.jp](http://sinsy.jp/) website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

You can find a sample merged with the instrumental audio [here](https://soundcloud.com/mathias-gatti/shallow-midi2voice).

## Requirements
- musescore: It's used to convert midi to musicxml

- python 3

- python libraries (Try something like: `pip install -r requirements.txt`)

## Usage
It is used running the main script `midi2voice.py`, it has four parameters, the lyrics_file, midi_file, singer sex (optional) and tempo (optional).

Usage example

```
python3 midi2voice.py ./inputs/shallow.txt ./inputs/shallow.mid female 96
```
