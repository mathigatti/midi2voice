from pydub import AudioSegment
from pydub.playback import play
import sys

audio2 = AudioSegment.from_file(LAST_INSTRUMENTAL_WAV, parameters=["-vol", "85"])
audio1 = AudioSegment.from_file(LAST_VOICE_WAV)

delay = 0
if len(sys.argv) > 1:
	delay = int(sys.argv[1])
mixed = audio1.overlay(audio2,delay)

mixed.export("sample.mp3", format="mp3")
play(mixed)