import os
import sys
import urllib

from voiceSpecificator import generateVoiceSpecification

# Constants
FILES_ROOT = "./tmp/"
VOICE_XML_ORIGINAL=FILES_ROOT + "last_voice.musicxml"
VOICE_XML_PROCESSED=FILES_ROOT+"last_voice.xml"

WAVS_ROOT = "./"
LAST_VOICE_WAV = WAVS_ROOT + "last_voice_generated.wav"

def renderizeVoice(lyrics,midiPath,sex, tempo):

	print("Running voice renderization")

	createMusicXML(midiPath,VOICE_XML_ORIGINAL)

	lyrics = tokenize(lyrics)

	generateVoiceSpecification(lyrics,tempo,VOICE_XML_ORIGINAL,VOICE_XML_PROCESSED)

	if sex == "male":
		urlfileName = os.popen("curl -X POST -F 'SPKR_LANG=english' -F 'SPKR=5' -F 'SYNALPHA=0.55' -F 'VIBPOWER=1' -F 'F0SHIFT=0' -F  'SYNSRC=@" + VOICE_XML_PROCESSED +"' http://sinsy.sp.nitech.ac.jp/index.php | grep 'lf0'").read()
	else:
		urlfileName = os.popen("curl -X POST -F 'SPKR_LANG=english' -F 'SPKR=4' -F 'SYNALPHA=0.55' -F 'VIBPOWER=1' -F 'F0SHIFT=0' -F  'SYNSRC=@" + VOICE_XML_PROCESSED +"' http://sinsy.sp.nitech.ac.jp/index.php | grep 'lf0'").read()

	download(urlfileName,LAST_VOICE_WAV)

	print("Finished voice renderization")

def download(output,wavPath):
	text = reduce(lambda accum,x: accum + x, output, "")
	index = text.find('./temp/') + len('./temp/')
	text = text[index:index+40].split(".")[0]

	testfile = urllib.URLopener()
	testfile.retrieve("http://sinsy.sp.nitech.ac.jp/temp/" + text + ".wav", wavPath)

def createMusicXML(midiPath, new_musicxml_path):
    os.system("musescore "+ midiPath +" -o " + new_musicxml_path)

def tokenize(text):
	textSyllables = cleanText(text)
	return filter(lambda x: len(x) > 0, textSyllables.replace(" ", "-").split("-"))

def cleanText(text):

	text.replace("\n"," ")
	text = text.lower()

	symbolsToDelete = ".,'!?" + '"'
	for symbol in symbolsToDelete:
		text = text.replace(symbol,"")

	return text

def main(textFilePath, midiPath, sex, tempo):

	with open(textFilePath, 'r') as text:
		lyrics = text.read()

	renderizeVoice(lyrics,midiPath,sex, tempo)


textFilePath = sys.argv[1]
midiPath = sys.argv[2]
sex = "female"
tempo = 80

if len(sys.argv) >= 4:	
	sex = sys.argv[3]
	if len(sys.argv) >= 5:
		tempo = int(sys.argv[4])

main(textFilePath, midiPath, sex, tempo)
