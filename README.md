# Singing Synthesis from MIDI file

This script relies on the sinsy.jp website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

You can find a sample merged with the instrumental audio [here](https://soundcloud.com/mathias-gatti/somebody-that-i-used-to-know-sinsy-synthetic-voice).

## Requirements
- musescore: It's used to convert midi to musicxml

- curl: It's used to make request to sinsy.jp

- python 3 (Python 2 can also be used with a few modifications, check [this](https://github.com/mathigatti/midi2voice/commit/94bd363bc887fbc8b3206d318a01a2ba77e970d5))

## Usage
It is used running the main script `midi2voice.py`, it has four parameters, the lyrics_file, midi_file, singer sex (optional) and tempo (optional).

Usage example

```
python midi2voice.py ./inputs/somebodyThatIUsedToKnow_lyrics.txt ./inputs/somebodyThatIUsedToKnow_voice.mid male 120
```
