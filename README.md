# Singing Synthesis from MIDI file

This script relies on the [sinsy.jp](http://sinsy.jp/) website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

You can find a sample merged with the instrumental audio [here](https://soundcloud.com/mathias-gatti/shallow-midi2voice).

## Requirements

- musescore: It's used to convert midi to musicxml
- python 3

## Installation

```bash
pip install git+git://github.com/mathigatti/midi2voice.git
```

## Usage

You can use it running the installed module using `python -m midi2voice`. It has serveral parameters, most are optional and you need to use them only if you want to specify something different than the default

```
python -m midi2voice
  -h, --help # show this help message and exit
  -l LYRICS, --lyrics LYRICS # Path to txt file containing the lyrics
  -m MIDI, --midi MIDI # Path to midi file
  -lang {english,japanese,mandarin} # Language of the voice (OPTIONAL / DEFAULT: english)
  -g {female,male} # Gender voice (female/male) (OPTIONAL / DEFAULT: female)
  -i VOICEINDEX # Each language has different voices, for example japanese has 4 different female voices at the moment, mandarin only one. (OPTIONAL / DEFAULT: 0)
  -t TEMPO # Song tempo in BPMs (OPTIONAL / DEFAULT 80)
  -s SYNALPHA # Gender parameter [between -0.8 and 0.8, default: 0.55]
  -v VIBPOWER # Vibrato intensity [between 0 and 2, default: 1]
  -p F0SHIFT # Pitch shift [in half tones, between -24 and 24, default: 0]
  -d DESTINATION_FOLDER # Destination folder
```

### Usage example

Check the midi and text samples [here](https://github.com/mathigatti/midi2voice/tree/master/inputs).

```bash
# Print help
python3 -m midi2voice -h

# Basic example
python -m midi2voice -l shallow.txt -m shallow.mid

# Generate the voice given a midi file and a text file with the lyrics
python -m midi2voice -l shallow.txt -m shallow.mid -lang english -g female -t 96
```

### Try it on Colab

If you don't have python installed or you just want to check it quickly you can try it online [here](https://colab.research.google.com/drive/1_lZiwQfuHIVaEFmAibPKUMprZ_0yU35L?usp=sharing).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_lZiwQfuHIVaEFmAibPKUMprZ_0yU35L?usp=sharing)

## Voices available

At the moment [sinsy.jp](http://sinsy.jp/) provides this voices. You can use the VOICEINDEX parameter to choose them.

- Japanese

    - Female

        * 0 - f00001j_dnn_beta4 : Yoko : Japanese
        * 1 - f00002j_dnn_beta4 : Xiang-Ling : Japanese
        * 2 - f01018j_dnn_beta4 : undefined : Japanese
        * 3 - f00001j : Yoko : Japanese
        * 4 - f00002j : Xiang-Ling : Japanese
        * 5 - f00004j_beta : Namine Ritsu S : Japanese
        * 6 - f00005j : undefined : Japanese

    - Male

        * 0 - m01083j_dnn_beta4 : undefined : Japanese
        * 1 - m01083j : undefined : Japanese

- English

    - Female

        * 0 - f00002e_dnn_beta4 : Xiang-Ling : English
        * 1 - f00002e : Xiang-Ling : English

    - Male

        * 0 - m00003e_beta : Matsuo-P : English

- Mandarin
    - Female

        * 0 - f00002m : Xiang-Ling : Chinese (Mandarin)

    - Male

        * None at the moment

## Credits
This source code was developed by Mathias Gatti ([@mathigatti](https://mathigatti.com)) if you use it please remember to cite me. For scientific publications you can use this DOI.

`Gatti, M. (2020). mathigatti/midi2voice v1.0.0 (v1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.3969003`

[![DOI](https://zenodo.org/badge/140364503.svg)](https://zenodo.org/badge/latestdoi/140364503)

## Support my work

If you want to help me to keep going developing and maintaining open-source projects you can contribute buying me some [ko-fi](https://ko-fi.com/mathigatti).

## License
MIT
