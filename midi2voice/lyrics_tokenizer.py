from collections import defaultdict

from music21 import converter, instrument, note, chord
import pyphen

dic = pyphen.Pyphen(lang='en')

def tokenize(text,midiPath):
	new_text = "" 
	i = 0
	for n in notesPerVerse(midiPath):
		verse = cleanText(text[i])
		new_text += "|".join(vocals(verse,n)) + "|"
		i = (i+1)%len(text)

	new_text = new_text.strip()
	return list(new_text.split("|"))

def notesPerVerse(midiFile):

	mid = converter.parse(midiFile)
	
	try:
		instruments = instrument.partitionByInstrument(mid)
		assert len(instruments.parts) == 1 # MIDI file must contain only vocals
		for instrument_i in instruments.parts:
		    notes_to_parse = instrument_i.recurse()

	except:		
		notes_to_parse = mid.flat.notes

	notes_per_verse = 8

	notes_to_parse = list(filter(lambda element : isinstance(element, note.Note) or isinstance(element, chord.Chord), notes_to_parse))

	firstBar = int(notes_to_parse[0].offset/4)

	notesPerCompass = defaultdict(int)
	for element in notes_to_parse:
		start = element.offset
		notesPerCompass[int((start-4*firstBar)/notes_per_verse)] += 1

	return list(notesPerCompass.values())

continuation = "-"

def extendWord(text):
	for extensibleEnding in ["all","oh","ah","ad","as","at","al","a","e","i","o","u"]:
		if text.endswith(extensibleEnding) or text.endswith(extensibleEnding+continuation):
			if text.endswith(continuation):
				additional = continuation
			else:
				additional = ""

			if len(extensibleEnding) > 1:
				return text[:-1*len(extensibleEnding) + 1 - len(additional)] + continuation, extensibleEnding + additional
			else:
				return text, extensibleEnding
	return text, None

def findSmallers(silabas):
    smallers = -1
    min = float('inf')
    for i in range(len(silabas)-1):
        if min > len(silabas[i]) + len(silabas[i+1]):
            min = len(silabas[i]) + len(silabas[i+1])
            smallers = i
    return i

def silabas_word(text):
    return dic.inserted(text).replace("-", continuation + "|").split("|")

def silabas_sentence(sentence):
    return sum([silabas_word(word) for word in sentence.split()],[])

def vocals(text,n):
	silabas = silabas_sentence(text)

	if len(silabas) == n:
	    return silabas
	elif len(silabas) < n:
	    if all([extendWord(silaba)[1] == None for silaba in silabas]):
	    	silabas += ["a"]	    	
	    index = len(silabas)-1
	    while(len(silabas) < n):
	        prevPart, extensiblePart = extendWord(silabas[index])
	        if extensiblePart:
	        	silabas = silabas[:index] + [prevPart, extensiblePart] + silabas[index+1:]
	        index = (index - 1) % len(silabas)         
	    return silabas
	else:
	    while(len(silabas) > n):
	        i = findSmallers(silabas)
	        silabas = silabas[:i] + [silabas[i] + silabas[i+1]] + silabas[i+2:]
	    return silabas     

def cleanText(text):
	text = text.lower()

	symbolsToDelete = '.,!?"'
	for symbol in symbolsToDelete:
		text = text.replace(symbol,"")

	return text
