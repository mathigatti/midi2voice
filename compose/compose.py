from genetic_music_core import *

import sys
sys.path.append('.')
from utils import *

fewSilences = lambda x: countSilences(x) < 2
notesMoveGradually = lambda x: notesMovementScore(x) < 2

defaultBaseScale = MAJOR_PENTATONIC
defaultMelodyScale = MAJOR

r1 = Rhythm("c")
motif1 = train(r1, fewSilences)
m1 = Melody(motif1, defaultMelodyScale)
melody1 = train(m1, notesMoveGradually)

r2 = Rhythm("c")
motif2 = train(r2, fewSilences)
m2 = Melody(motif2, defaultMelodyScale)
melody2 = train(m2, notesMoveGradually)

motifs = [[motif1,melody1],[motif2,melody2]]

c = Composer(motifs, defaultBaseScale)

song = c.song
melodies = [song["MM"],song["BM"]]
rhythms = [song["MR"],song["BR"]]

voiceMelody = [song["BM"]]
voiceRhythm = [song["BR"]]

BPM = 200

def silenceToTempo(char):
    if char == "S":
        return 4
    elif char == "s":
        return 2
    else:
        return 1
        
def toList(rhythms, melodies, repetitions, total):
    lista = []
    for k in range(repetitions):
        for j in range(len(rhythms)):
            rhythm = rhythms[j]
            melody = melodies[j]
            time = 0 + total*k
            for i in range(len(rhythm)):
                char = rhythm[i]
                if char.isdigit():
                    dur = int(char)
                    note = int(melody[i])
                    lista.append([(note,dur,100, time)])
                    time += dur
                else:
                    time += silenceToTempo(char)
    return lista


def splitNote(nota):
    i = 0
    while not nota[i].isdigit():
        i+=1
    return (nota[:i], int(nota[i:]))

def voiceComposition(tuplas):

    print(tuplas)

    notas = []
    ritmos = []
    for tupla in tuplas:
        tupla = tupla[0]
        next = 0
        ritmo = []
        while next < 4:
            if tupla[-1]%4 > next:
                notas.append(-1)
                ritmo.append(tupla[-1]%4 - next)

                next += tupla[-1]%4 - next

            nota = midi2ScientificNotation[tupla[0]]
            nota = splitNote(nota)
            notas.append(nota)
            ritmo.append(tupla[1])

            next += tupla[1]
        ritmos.append(ritmo[:])

    return {'lyrics':'hello world','tempo':BPM,'rhythms':ritmos, 'notes':notas}

from midiPlayer import playSong
from midiPlayer import createMidi
import json


repetitions = 3

composition = toList(rhythms, melodies, repetitions, 24)

with open(LAST_VOICE_COMPOSITION, 'w') as lastVoiceComposition:
    voiceComp = toList(voiceRhythm, voiceMelody, repetitions, 24)
    json.dump(voiceComposition(voiceComp), lastVoiceComposition)

output_keyboard = 'keyboard_' + tag() + '.mid'
createMidi(MIDIS_ROOT + output_keyboard, composition, BPM)
createMidi(LAST_MIDI, composition, BPM)

playSong(LAST_MIDI)
