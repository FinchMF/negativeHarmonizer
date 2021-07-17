from negativeHarmonizer import ( ReHarmonizer, argparse )

def runNegatives(MIDI: str, negMIDI: str, notes: int=1, key: str=None):
    """Program to Generative Negative Harmony """
    ReHarmonizer(Inf=MIDI, Outf=negMIDI, notes=notes, key=key)

if __name__ == '__main__':
    # takes in midi file and output midi | runs negative
    # with option of note detail and key
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '-midi_in', type=str, 
                      help='name of midi file to be reharmonized')
    parser.add_argument('-o', '-midi_out', type=str,
                      help='name of midi file where rehamonized midi will be save to \
                           | do not add .mid extension')
    parser.add_argument('-n', '-note_detail', type=int, default=1,
                      help='decides how the midi note_on and note_off data is treated')
    parser.add_argument('-k', '-key', type=str, default=None,
                      help='choose what key should act as root in order to decide the \
                           pivot point of negsative harmony\'s transformative axis')
    
    args = parser.parse_args()
   
    runNegatives(MIDI=args.i, negMIDI=args.o,
                 notes=args.n, key=args.k)     