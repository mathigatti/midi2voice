# -*- coding: latin-1 -*-

from lyrics_tokenizer import tokenize

import re
import os

def midi2xml(lyrics,midiPath,xmlPath,tempo):
	tempXML = "temp.xml"
	createMusicXML(midiPath,tempXML)
	lyrics = tokenize(lyrics,midiPath)
	generateVoiceSpecification(lyrics,tempo,tempXML,xmlPath)
	os.remove(tempXML)

def createMusicXML(midiPath, new_musicxml_path):
    os.system("export QT_QPA_PLATFORM=offscreen && musescore "+ midiPath +" -o " + new_musicxml_path)

def generateVoiceSpecification(lyrics,tempo,inputMusicXMLPath,outputMusicXMLPath):
	with open(inputMusicXMLPath, 'r') as c:
		content = [x.strip() for x in c.readlines()]
		with open(outputMusicXMLPath,'w') as f:
			f.write(addVoiceTags(tempo,lyrics,content))

def addVoiceTags(tempo, text, content):
	print("Text:\n" + str(text))
	output = ""
	lyrics_xml = '<voice>1</voice>\n<lyric>\n<syllabic>{}</syllabic>\n<text>{}</text>\n</lyric>\n'

	i = 0
	ignoreThisNote = False
	prevBeginning = False
	for line in content:
		if "<rest/>" in line or '<tie type="stop"/>' in line:
			ignoreThisNote = True
		if "</note" in line:
			if not ignoreThisNote:
				nextPart = text[i%len(text)]
				if nextPart.endswith("-"):
					nextPart = nextPart[:-1]
					if prevBeginning:
						syllabic = "middle"
					else:
						syllabic = "begin"
						prevBeginning = True
				else:
					if prevBeginning:
						syllabic = "end"
					else:
						syllabic = "single"
					prevBeginning = False
				output += lyrics_xml.format(syllabic,nextPart)
				i+=1
			else:
				ignoreThisNote = False

		output += line

	output = re.sub(r"<per-minute>\d+</per-minute>", f"<per-minute>{tempo}</per-minute>",output)
	output = re.sub(r'<sound tempo="\d+"/>', f'<sound tempo="{tempo}"/>',output)

	return output
