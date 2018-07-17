
# Constants
VOICE_XML_ROOT_PATH = "inputs/musicXMLs/"
WAVS_ROOT = "output/"
LAST_VOICE_WAV = WAVS_ROOT + "voice_last_recording.wav"

import time
import datetime

def tag():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
