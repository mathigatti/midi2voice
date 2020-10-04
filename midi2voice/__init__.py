import os
import sys
import urllib.request
import requests

from .midi2xml import midi2xml

def renderize_voice(lyrics, midi_path, sex="female", tempo=80, out_folder="."):
	VOICE_XML_PATH = os.path.join(out_folder,"voice.xml")
	VOICE_WAV_PATH = os.path.join(out_folder,"voice.wav")

	midi2xml(lyrics,midi_path,VOICE_XML_PATH,tempo)
	sinsy_request(VOICE_XML_PATH, VOICE_WAV_PATH,sex)

def sinsy_request(xml_file_path, wav_path, sex):
	if sex == "male":
		SPKR = 5
	else:
		SPKR = 4

	headers = {'User-Agent': 'Mozilla/5.0'}
	payload = {'SPKR_LANG':'english', 'SPKR':SPKR, 'VIBPOWER':'1', 'F0SHIFT':'0'}
	files = {'SYNSRC': open(xml_file_path,'rb')}

	# Sending post request and saving response as response object 
	r = requests.post(url='http://sinsy.sp.nitech.ac.jp/index.php', headers=headers, data=payload, files=files)
	html_response = r.text.split("temp/")

	# Magic scraping of the website to find the name of the wav file generated
	url_file_name = find_wav_name_on_website(html_response)

	if url_file_name is None:
		raise Exception("No wav file found on sinsy.jp")
	else:
		download(url_file_name, wav_path)

def find_wav_name_on_website(htmlResponse):
	url_file_name = None
	for line in htmlResponse:
		parts = line.split(".")
		if parts[1][:3] == "wav":
			url_file_name = parts[0]
			break
	return url_file_name

def download(url_file_name, wav_path):
	urllib.request.urlretrieve("http://sinsy.sp.nitech.ac.jp/temp/" + url_file_name + ".wav", wav_path)