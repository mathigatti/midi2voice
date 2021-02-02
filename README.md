# Singing Synthesis from MIDI file

This script relies on the [sinsy.jp](http://sinsy.jp/) website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

You can find a sample merged with the instrumental audio [here](https://soundcloud.com/mathias-gatti/shallow-midi2voice).

## Requirements

- musescore: It's used to convert midi to musicxml
- python 3

## Installation

```bash
pip install midi2voice
```

## Usage

You can use it running the installed module using `python -m`. It has five parameters, the lyrics_file, midi_file, singer sex (optional), tempo (optional) and destination folder (optional).

### Usage example

Check the midi and text samples [here](https://github.com/mathigatti/midi2voice/tree/master/inputs).

```bash
# Print help
python3 -m midi2voice -h

# Generate the voice given a midi file and a text file with the lyrics
python -m midi2voice -l shallow.txt -m shallow.mid -g female -t 96
```

## Try it on Colab

If you don't have python installed or you just want to check it quickly you can try it online [here](https://colab.research.google.com/drive/1_lZiwQfuHIVaEFmAibPKUMprZ_0yU35L?usp=sharing).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_lZiwQfuHIVaEFmAibPKUMprZ_0yU35L?usp=sharing)

## Credits
This source code was developed by Mathias Gatti ([@mathigatti](https://mathigatti.com)) if you use it please remember to cite me. For scientific publications you can use this DOI.

`Gatti, M. (2020). mathigatti/midi2voice v1.0.0 (v1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.3969003`

[![DOI](https://zenodo.org/badge/140364503.svg)](https://zenodo.org/badge/latestdoi/140364503)

## Support my work

If you want to help me to keep going developing and maintaining open-source projects you can contribute buying me some [ko-fi](https://ko-fi.com/mathigatti).

## License
MIT
