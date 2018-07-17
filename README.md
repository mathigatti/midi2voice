# Singing Synthesis from MIDI file

This script relies on the sinsy.jp website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

## Requirements
	* Extra software
		- musescore: 
		- curl
	
	* python 2.7
	* python libaries
		- subprocess
		- datetime
		- urllib
		- hyphenator



## Usage
It is used running the main script ./voice.sh, it has three parameters, the lyrics_file, midi_file and tempo.

Usage example
	./voice.sh inputs/lyrics/somebodyThatIUsedToKnow_lyrics.txt inputs/midi/somebodyThatIUsedToKnow_voice.mid 120
