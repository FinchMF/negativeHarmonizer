from negativeHarmonizer import ( mido, MidiFile, Negator )

def readIn(f: str) -> mido.midifiles.midifiles.MidiFile:
    """Function to read in MidiFile"""
    return MidiFile(f)

def readOut(midiFile: mido.midifiles.midifiles.MidiFile, f: str):
    """Function to save midifile"""
    midiFile.save(f"{f}.mid")

def flip(midiFile: mido.midifiles.midifiles.MidiFile) -> mido.midifiles.midifiles.MidiFile:
    """Function to convert each midi note into its negative counterpart"""
    converter = None
    for event in midiFile:

        if event.type == 'key_signature':
            converter = Negator(key=event.key)

        if event.type == 'note_on' or event.type == 'note_off':

            event.note = Negator.convert(midi_n=int(event.note))

    return midiFile

class ReHarmonizer:
    """Object to reharmonize with Negative Harmony"""
    def __init__(self, Inf: str, Outf: str):

        self.inf = Inf
        self.outf = Outf
        self.convert()

    def convert(self):
        """function to convert"""
        midiFile = readIn(f=self.inf)
        midiFile = flip(midiFile=midiFile)
        readOut = readOut(midiFile=midiFile, f=self.outf)