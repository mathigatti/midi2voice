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
ap.add_argument("-s", "--synalpha", required=False, default=0.55,
   help="Gender parameter. Float: [-0.8, 0.8]")
ap.add_argument("-v", "--vibpower", required=False, default=1,
   help="Vibrato intensity. Float: [0, 2]")
ap.add_argument("-p", "--pitch", required=False, default=0,
   help="Pitch shift, in half tones. Integer: [-24, 24]")
ap.add_argument("-d", "--destination_folder", required=False, default='.',
   help="Destination folder")
args = vars(ap.parse_args())

with open(args['lyrics'], 'r') as text:
	lyrics = text.readlines()

renderize_voice(lyrics, args['midi'], int(args['tempo']), args['language'], args['gender'], int(args['voiceindex']),
                args['destination_folder'], float(args['vibpower']), int(args['pitch']), float(args['synalpha']))
