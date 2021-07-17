from negativeHarmonizer import ( sys, ReHarmonizer )

def runNegatives(MIDI: str, negMIDI: str, notes: int=1):
    """Program to Generative Negative Harmony """
    ReHarmonizer(Inf=MIDI, Outf=negMIDI, notes=notes)

if __name__ == '__main__':
    # takes in midi file and output midi | runs negative
    if sys.argv[3]:
        runNegatives(MIDI=sys.argv[1],
                    negMIDI=sys.argv[2],
                    notes=int(sys.argv[3]))
    else:
        runNegatives(MIDI=sys.argv[1],
                    negMIDI=sys.argv[2])