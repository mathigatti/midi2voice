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

## Try it on Colab

If you don't have python installed or you just want to check it quickly you can try it online [here](https://colab.research.google.com/drive/1_lZiwQfuHIVaEFmAibPKUMprZ_0yU35L?usp=sharing).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_lZiwQfuHIVaEFmAibPKUMprZ_0yU35L?usp=sharing)

## Credits
This source code is developed by Mathias Gatti ([@mathigatti](https://mathigatti.com)) if you use it please remember to cite me. For scientific publications you can use this DOI.

[![DOI](https://zenodo.org/badge/140364503.svg)](https://zenodo.org/badge/latestdoi/140364503)

## Support my work

Mathias's open-source projects are supported by [his Patreon](https://www.patreon.com/mathigatti). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.

## License
MIT
