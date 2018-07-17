import sys
sys.path.append('.')
from utils import *
import subprocess

output = WAVS_ROOT + 'voice_' + tag() + '.wav'
subprocess.Popen("cp " + LAST_VOICE_WAV + " " + output, shell=True)