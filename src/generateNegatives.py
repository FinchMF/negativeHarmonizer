from negativeHarmonizer import ( sys, ReHarmonizer )

def runNegatives(MIDI: str, negMIDI: str):
    """Program to Generative Negative Harmony """
    ReHarmonizer(Inf=MIDI, Outf=negMIDI)

if __name__ == '__main__':
    # takes in midi file and output midi | runs negative
    runNegatives(MIDI=sys.argv[1],
                 negMIDI=sys.argv[2])