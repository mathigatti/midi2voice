"""
Music Scales

Source: http://en.wikipedia.org/wiki/List_of_musical_scales_and_modes

Copyright (C) 2012  Alfred Farrugia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

ACOUSTIC_SCALE = [0, 2, 4, 6, 7, 9, 10]
ADONAI_MALAKH = [0, 2, 4, 5, 7, 8, 10]
AEOLIAN_MODE = [0, 2, 3, 5, 7, 8, 10]
ALGERIAN_SCALE = [0, 2, 3, 6, 7, 8, 11]
ALTERED_SCALE = [0, 1, 3, 4, 6, 8, 10]
AUGMENTED_SCALE = [0, 3, 4, 7, 8, 11]
BEBOP_DOMINANT = [0, 2, 4, 5, 7, 9, 10, 11]
BLUES_SCALE = [0, 3, 5, 6, 7, 10]
DORIAN_MODE = [0, 2, 3, 5, 7, 9, 10]
DOUBLE_HARMONIC_SCALE = [0, 1, 4, 5, 7, 8, 11]
ENIGMATIC_SCALE = [0, 1, 4, 6, 8, 10, 11]
FLAMENCO_MODE = [0, 1, 4, 5, 7, 8, 11]
GYPSY_SCALE = [0, 2, 3, 6, 7, 8, 10]
HALF_DIMINISHED_SCALE = [0, 2, 3, 5, 6, 8, 10]
HARMONIC_MAJOR_SCALE = [0, 2, 4, 5, 7, 8, 11]
HARMONIC_MINOR_SCALE = [0, 2, 3, 5, 7, 8, 11]
HIRAJOSHI_SCALE = [0, 4, 6, 7, 11]
HUNGARIAN_GYPSY_SCALE = [0, 2, 3, 6, 7, 8, 11]
INSEN_SCALE = [0, 1, 5, 7, 10]
IONIAN_MODE = [0, 2, 4, 5, 7, 9, 11]
IWATO_SCALE = [0, 1, 5, 6, 11]
LOCRIAN_MODE = [0, 1, 3, 5, 6, 8, 10]
LYDIAN_AUGMENTED_SCALE = [0, 2, 4, 6, 8, 9, 11]
LYDIAN_MODE = [0, 2, 4, 6, 7, 9, 11]
MAJOR_LOCRIAN = [0, 2, 4, 5, 6, 8, 10]
MELODIC_MINOR_SCALE = [0, 2, 3, 5, 7, 9, 11]
MIXOLYDIAN_MODE = [0, 2, 4, 5, 7, 9, 10]
NEAPOLITAN_MAJOR_SCALE = [0, 1, 3, 5, 7, 9, 11]
NEAPOLITAN_MINOR_SCALE = [0, 1, 3, 5, 7, 8, 11]
PERSIAN_SCALE = [0, 1, 4, 5, 6, 8, 11]
PHRYGIAN_MODE = [0, 1, 3, 5, 7, 8, 10]
PROMETHEUS_SCALE = [0, 2, 4, 6, 9, 10]
TRITONE_SCALE = [0, 1, 4, 6, 7, 10]
UKRAINIAN_DORIAN_SCALE = [0, 2, 3, 6, 7, 9, 10]
WHOLE_TONE_SCALE = [0, 2, 4, 6, 8, 10]
MAJOR = [0, 2, 4, 5, 7, 9, 11]
MAJOR_PENTATONIC = [0,2,4,7,9]
MINOR = [0, 2, 3, 5, 7, 8, 10]
MINOR_PENTATONIC = [0,3,5,7,10]

scientificNotation2midi = {"C0" : 0, "C#0" : 1, "D0" : 2,
		"D#0" : 3, "E0" : 4, "F0" : 5,
		"F#0" : 6, "G0" : 7, "G#0" : 8,
		"A0" : 9, "A#0" : 10, "B0" : 11,
		"C1" : 12, "C#1" : 13, "D1" : 14,
		"D#1" : 15, "E1" : 16, "F1" : 17,
		"F#1" : 18, "G1" : 19, "G#1" : 20,
		"A1" : 21, "A#1" : 22, "B1" : 23,
		"C2" : 24, "C#2": 25, "D2" : 26,
		"D#2" : 27, "E2" : 28, "F2" : 29,
		"F#2" : 30, "G2" : 31, "G#2" : 32,
		"A2" : 33, "A#2" : 34, "B2" : 35,
		"C3" : 36, "C#3" : 37, "D3" : 38,
		"D#3" : 39, "E3" : 40, "F3" : 41,
		"F#3" : 42, "G3" : 43, "G#3" : 44,
		"A3" : 45, "A#3" : 46, "B3" : 47,
		"C4" : 48, "C#4" : 49, "D4" : 50,
		"D#4" : 51, "E4" : 52, "F4" : 53,
		"F#4" : 54, "G4" : 55, "G#4" : 56,
		"A4" : 57, "A#4" : 58, "B4" : 59,
		"C5" : 60, "C#5" : 61, "D5" : 62,
		"D#5" : 63, "E5" : 64, "F5" : 65,
		"F#5" : 66, "G5" : 67, "G#5" : 68,
		"A5" : 69, "A#5" : 70, "B5" : 71,
		"C6" : 72, "C#6" : 73, "D6" : 74,
		"D#6" : 75, "E6" : 76, "F6" : 77,
		"F#6" : 78, "G6" : 79, "G#6" : 80,
		"A6" : 81, "A#6" : 82, "B6" : 83,
		"C7" : 84, "C#7" : 85, "D7" : 86,
		"D#7" : 87, "E7" : 88, "F7" : 89,
		"F#7" : 90, "G7" : 91, "G#7" : 92,
		"A7" : 93, "A#7" : 94, "B7" : 95,
		"C8" : 96, "C#8" : 97, "D8" : 98,
		"D#8" : 99, "E8" : 100, "F8" : 101,
		"F#8" : 102, "G8" : 103, "G#8" : 104,
		"A8" : 105, "A#8" : 106, "B8" : 107,
		"C9" : 108, "C#9" : 109, "D9" : 110,
		"D#9" : 111, "E9" : 112, "F9" : 113,
		"F#9" : 114, "G9" : 115, "G#9" : 116,
		"A9" : 117, "A#9" : 118, "B9" : 119,
		"C10" : 120, "C#10" : 121, "D10" : 122,
		"D#10" : 123, "E10" : 124, "F10" : 125,
		"F#10" : 126, "G10" : 127}

midi2ScientificNotation = {v: k for k, v in scientificNotation2midi.items()}

"""
Build a scale given an array s

Example: to build a scale between 0 and 128 using the notes C, D, E

buildScale([0,2,4],0,128)
"""


def buildScale(s, min_note=0, max_note=128):
    return [x + (12 * j)
        for j in range(12)
        for x in s
        if x + (12 * j) >= min_note and x + (12 * j) <= max_note]
