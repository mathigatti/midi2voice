import sys
sys.path.append('.')
from utils import *
import time
import subprocess

def midi2wav(input_file, output_file):
    subprocess.Popen("timidity " + input_file + " -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k " + output_file, shell=True)
    time.sleep(1)
    subprocess.Popen("cp " + output_file + " " + LAST_INSTRUMENTAL_WAV, shell=True)

output = 'instrumental_' + tag() + '.wav'
midi2wav(LAST_MIDI, WAVS_ROOT + output)