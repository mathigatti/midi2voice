
# Constants
MIDIS_ROOT = "compose/midis/"
VOICE_COMPOSITION_ROOT = "compose/voice/"
WAVS_ROOT = "generateSong/wavs/"
VOICE_ROOT_PATH = "generateSong/voice/"
VOICE_XML_ROOT_PATH = "generateSong/voice/musicXMLs/"
LAST_MIDI = MIDIS_ROOT + "keyboard_last_recording.mid"
LAST_VOICE_COMPOSITION =  VOICE_COMPOSITION_ROOT + "voice_last_composition.json"
LAST_INSTRUMENTAL_WAV = WAVS_ROOT + "instrumental_last_recording.wav"
LAST_VOICE_WAV = WAVS_ROOT + "voice_last_recording.wav"

import time
import datetime

def tag():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
