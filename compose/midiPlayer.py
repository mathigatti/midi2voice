import pygame, sys

def play(music_file):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
    except pygame.error:
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(120)

def playSong(midi_file):

    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024    # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        play(midi_file)
    except KeyboardInterrupt:
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()


from midiutil.MidiFile import MIDIFile

# Example composition
# [[(60,1,100),(62,1,100),(64,1,100)],[],[(67,2,100)]]

#tempo in BPM

def createMidi(midi_file, composition, tempo, instrumentCode=24):
    track    = 0
    channel  = 0
    MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                         # automatically created)
    MyMIDI.addProgramChange(track, channel, -1, instrumentCode)

    time = 0   # In beats
    MyMIDI.addTempo(track,time, tempo)
    for notes in composition:
        for note in notes:
            pitch = note[0]
            duration = note[1]   # In beats
            volume   = note[2] # 0-127, as per the MIDI standard
            time = note[3]

            MyMIDI.addNote(track, channel, pitch, time, duration, volume)

    with open(midi_file, "wb") as output_file:
        MyMIDI.writeFile(output_file)