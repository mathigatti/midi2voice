# -*- coding: latin-1 -*-
import math
import sys

import sys
sys.path.append('.')
from utils import *
from hyphenator import Hyphenator

def separarEnSilabas(text):
	h = Hyphenator("/usr/share/myspell/dicts/hyph_en_US.dic")
	textSyllables = h.inserted(text)
	return filter(lambda x: len(x) > 0, textSyllables.replace(" ", "-").split("-"))

xmlSpecPath = VOICE_ROOT_PATH + "xmlSpecs/"

f = open(xmlSpecPath + 'compasBeginning.xml', 'r')
compasBeginning = f.read()
f.close()

f = open(xmlSpecPath + 'compasEnd.xml', 'r')
compasEnd = f.read()
f.close()

f = open(xmlSpecPath + 'compasNote.xml', 'r')
compasNote = f.read()
f.close()

f = open(xmlSpecPath + 'compasNoteSilence.xml', 'r')
compasNoteSilence = f.read()
f.close()

f = open(xmlSpecPath + 'finalMusicXML.xml', 'r')
finalMusicXML = f.read()
f.close()

f = open(xmlSpecPath + 'initialMusicXML.xml', 'r')
initialMusicXML = f.read()
f.close()

def musicXML(tempo, compases, melody, text):
	output = initialMusicXML
	output.format(tempo,tempo)

	noteIndex = 0
	for i in range(len(compases)):
		output += compasBeginning.format(str(i+2))

		for j in range(len(compases[i])):
			if melody[noteIndex] != -1:

				note, octave = melody[noteIndex]
				duration = compases[i][j]

				output += compasNote.format(tempo,note,str(octave),str(duration),text[noteIndex])
			else:
				duration = compases[i][j]

				output += compasNoteSilence.format(tempo,str(duration))

			noteIndex += 1
		output += compasEnd

	return output + finalMusicXML.format(str(len(compases)+3))

def musicGenerator(tempo, compases, melody, text):

	assert reduce(lambda accum, x: accum+len(x), compases,0) == len(melody)

	text = separarEnSilabas(text)
	if len(text) < len(melody):
		text = (text*int(math.ceil(len(melody)/float(len(text)))))[:len(melody)]
	print text

	return musicXML(tempo, compases,melody,text)

import json
with open(LAST_VOICE_COMPOSITION, 'r') as c:
	composition = json.load(c)
	with open(VOICE_XML_ROOT_PATH+'voice.xml','w') as f:
		f.write(musicGenerator(composition['tempo'], composition['rhythms'][2:], composition['notes'][2:],composition['lyrics']))
