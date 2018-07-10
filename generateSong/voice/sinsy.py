import sys
sys.path.append('.')
from utils import *

text = reduce(lambda accum,x: accum + x, sys.argv[1:], "")
print text
index = text.find('./temp/') + len('./temp/')
print text
text = text[index:index+40].split(".")[0]
print text

import urllib
import pygame
import time
testfile = urllib.URLopener()
testfile.retrieve("http://sinsy.sp.nitech.ac.jp/temp/" + text + ".wav", LAST_VOICE_WAV)