import random
from Scales import *

def isNote(char):
    return char.isdigit()

class Rhythm:
    rules = {"f":["cccc"], "c": ["mmmmmmmm", "nnnn", "NN"], "N":["mmmm", "nn", "4", "S"], "n":["mm", "s", "2"], "m":["1","z"]}
    nonFinalChars = ["f", "c", "N", "n", "m"]
    
    def __init__(self, initial):
        self.song = initial
    
    def detectNonFinalChars(self):
        nonFinalsCharsIndexes = []
        for i in range(len(self.song)):
            if self.song[i] in self.nonFinalChars:
                nonFinalsCharsIndexes.append(i)
        return nonFinalsCharsIndexes
    
    def applySomeRule(self):
        i = random.choice(self.detectNonFinalChars())
        char = self.song[i]
        self.song = self.song[0:i] + random.choice(self.rules[char]) + self.song[i+1:]
        
class Melody:

    def __init__(self, rhythm, scale):
        self.scale = buildScale(scale, min_note=48, max_note=72)
        self.rhythm = rhythm
        self.song = self.initialMelody(rhythm)
        
    def initialMelody(self,rhythm):
        melody = []
        for char in rhythm:
            if isNote(char):
                melody.append("_")
            else:
                melody.append(char)
        return melody
    
    def detectNonFinalChars(self):
        noteCharsIndexes = []
        for i in range(len(self.song)):
            if self.song[i] == "_":
                noteCharsIndexes.append(i)
        return noteCharsIndexes
    
    def applySomeRule(self):
        i = random.choice(self.detectNonFinalChars())
        char = self.song[i]
        self.song = self.song[0:i] + [str(random.choice(self.scale))] + self.song[i+1:]    
        
class Composer:
    structure = ["B1", "B2", "R"]
    
    def __init__(self, motifs, scale):
        self.scale = buildScale(scale, min_note=48, max_note=72)
        self.motifs = motifs
        self.song = self.initialComposition(motifs, self.scale)
        
    def initialComposition(self, motifs,scale):
        
        motifsLengh = 8
        baseNotesDuration = 4

        baseMelody = []
        baseRhythm = []
        mainMelody = []
        mainRhythm = []
        
        compositionMotifs = {}
        compositionMotifs["B1"] = random.choice(motifs)
        compositionMotifs["B2"] = random.choice(motifs)
        compositionMotifs["R"] = random.choice(motifs)
        
        for part in self.structure:
            mainRhythm += compositionMotifs[part][0]
            mainMelody += [str(int(note) + 12) if isNote(note) else note for note in compositionMotifs[part][1]]
            melody = [int(note) for note in compositionMotifs[part][1] if isNote(note)]
            for i in range(motifsLengh//baseNotesDuration):
                baseNote = random.choice(list(filter(lambda x: x in scale,melody))+[scale[0]])
                baseRhythm += [str(baseNotesDuration)]
                baseMelody += [str(baseNote)]

        return {"BM":baseMelody, "BR":baseRhythm, "MM":mainMelody, "MR":mainRhythm}
    
    
    def tonalBase():   
        return self.baseMelody
    
    def goodEnough(self):
        return tonalBase()
    
    def applySomeRule(self):
        if not self.goodEnough():
                return True

def train(s, condition):
    while len(s.detectNonFinalChars()) > 0:
        song = s.song
        s.applySomeRule()
        if not condition(s.song):
            s.song = song
    return s.song


def countSilences(x):
    silenceValues = {"S":4, "s":2,"z":1}
    res = 0
    for char in x:
        if char in silenceValues:
            res += silenceValues[char]
    return res

def notesMovementScore(x):
    previousNote = -1
    n = 0
    totalScore = 0
    for note in x:
        if isNote(note) and previousNote != -1:
            n += 1
            totalScore += abs(int(note) - previousNote) - 3
    return totalScore/(n+0.00001)
