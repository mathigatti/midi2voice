import argparse

from . import renderize_voice

ap = argparse.ArgumentParser()

ap.add_argument("-l", "--lyrics", required=True,
   help="Path to txt file containing the lyrics")
ap.add_argument("-m", "--midi", required=True,
   help="Path to midi file")
ap.add_argument("-lang", "--language", required=False, default="english", choices=['english', 'japanese', 'mandarin'],
   help="Language of the voice (english/japanese/mandarin)")
ap.add_argument("-g", "--gender", required=False, default="female", choices=['female', 'male'],
   help="Gender voice (female/male)")
ap.add_argument("-i", "--voiceindex", required=False, default=0,
   help="Each language has different voices, for example japanese has 7 different female voices at the moment, mandarin only one.")
ap.add_argument("-t", "--tempo", required=False, default=80,
   help="Song tempo in BPMs")
ap.add_argument("-d", "--destination_folder", required=False, default='.',
   help="Destination folder")
args = vars(ap.parse_args())

with open(args['lyrics'], 'r') as text:
	lyrics = text.readlines()

renderize_voice(lyrics, args['midi'], int(args['tempo']), args['language'], args['gender'], args['voiceindex'], args['destination_folder'])