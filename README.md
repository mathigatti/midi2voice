# Singing Synthesis from MIDI file

This script relies on the sinsy.jp website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

## Requirements
- musescore
    It's used to convert midi to musicxml
- curl
    It's used to make request to sinsy.jp
- python 2.7 and libraries
	- subprocess
	- datetime
	- urllib
	- hyphenator

## Usage
It is used running the main script ./voice.sh, it has three parameters, the lyrics_file, midi_file and tempo.

Usage example

```
./voice.sh inputs/lyrics/somebodyThatIUsedToKnow_lyrics.txt inputs/midi/somebodyThatIUsedToKnow_voice.mid 120
```

You can find a sample merged with the instrumental audio [here](https://soundcloud.com/mathias-gatti/somebody-that-i-used-to-know-sinsy-synthetic-voice).
