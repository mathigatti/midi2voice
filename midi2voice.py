import os
import sys
import urllib.request
from voiceSpecificator import generateVoiceSpecification
from functools import reduce
import requests

# Constants
FILES_ROOT = "./tmp/"
VOICE_XML_ORIGINAL=FILES_ROOT + "last_voice.xml"
VOICE_XML_PROCESSED=FILES_ROOT+"last_voice_processed.xml"

WAVS_ROOT = "./output/"
LAST_VOICE_WAV = WAVS_ROOT + "last_voice_generated.wav"

def renderizeVoice(lyrics,midiPath,sex,tempo):

	print("Running voice renderization")

	createMusicXML(midiPath,VOICE_XML_ORIGINAL)

	lyrics = tokenize(lyrics)

	generateVoiceSpecification(lyrics,tempo,VOICE_XML_ORIGINAL,VOICE_XML_PROCESSED)

	if sex == "male":
		request(VOICE_XML_PROCESSED, LAST_VOICE_WAV,"male")
	else:
		request(VOICE_XML_PROCESSED, LAST_VOICE_WAV,"female")

	print("Finished voice renderization")

def request(xml_file_path,wavPath,sex="female"):
	if sex == "male":
		SPKR = 5
	else:
		SPKR = 4

	headers = {'User-Agent': 'Mozilla/5.0'}
	payload = {'SPKR_LANG':'english', 'SPKR':SPKR, 'VIBPOWER':'1', 'F0SHIFT':'0'}
	files = {'SYNSRC': open(xml_file_path,'rb')}

	# Sending post request and saving response as response object 
	r = requests.post(url = 'http://sinsy.sp.nitech.ac.jp/index.php',headers=headers,data=payload,files=files)
	htmlResponse = r.text.split("temp/")

	# Magic scraping of the website to find the name of the wav file generated
	urlfileName = findWavNameOnWebsite(htmlResponse)

	if urlfileName is None:
		raise Exception("No wav file found on sinsy.jp")
	else:
		download(urlfileName,wavPath)

def findWavNameOnWebsite(htmlResponse):
	urlfileName = None
	for line in htmlResponse:
		parts = line.split(".")
		if parts[1][:3] == "wav":
			urlfileName = parts[0]
			break
	return urlfileName

def download(urlfileName,wavPath):
	urllib.request.urlretrieve("http://sinsy.sp.nitech.ac.jp/temp/" + urlfileName + ".wav", wavPath)

def createMusicXML(midiPath, new_musicxml_path):
    os.system("export QT_QPA_PLATFORM=offscreen && musescore "+ midiPath +" -o " + new_musicxml_path)

def tokenize(text):
	textSyllables = cleanText(text)
	return list(filter(lambda x: len(x) > 0, textSyllables.replace(" ", "-").split("-")))

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
