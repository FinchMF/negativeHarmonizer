from negativeHarmonizer import ( mido, MidiFile, MidiTrack, Negator, logger )

def readIn(f: str) -> mido.midifiles.midifiles.MidiFile:
    """Function to read in MidiFile"""
    return MidiFile(f)

def readOut(midiFile: mido.midifiles.midifiles.MidiFile, f: str):
    """Function to save midifile"""
    midiFile.save(f"{f}.mid")


def flip(midiFile: mido.midifiles.midifiles.MidiFile, 
         outMidi: mido.midifiles.midifiles.MidiFile, 
         notes: int, key: str=None) -> mido.midifiles.midifiles.MidiFile:
    """Function to convert each midi note into its negative counterpart"""
    # set the type of note data to look at
    if notes == 1:
        notes: list = ['note_on']
    else:
        notes: list = ['note_on', 'note_off']
    # transfer header data
    outMidi.type: str = midiFile.type
    outMidi.ticks_per_beat: int = midiFile.ticks_per_beat
    outMidi.charset: str = midiFile.charset
    converter = None
    # iterate through tracks in the midi file
    for track in midiFile.tracks:
        # per track set up the copy
        newtrack: object = MidiTrack()
        # iteratae through midi messages in track
        for event in track:
            # set converter based on key (this can change through out the peice)
            if event.type == 'key_signature':
                signature = event.key if not key else key
                converter: object = Negator(key=signature)
                newtrack.append(event.copy())
            # convert the pitch, then transfer data
            if event.type in notes: 
                prev: int = event.note
                try:
                    converted: int = converter.convert(midi_n=int(prev))
                except:
                    logger.info(f'A Key was Not Established in the Midi file,\
                                 so we are going to cross our fingers and go with root C')
                    signature = 'C' if not key else key
                    converter: object = Negator(key=signature)
                    converted: int = converter.convert(midi_n=int(prev))
                newtrack.append(event.copy( note = converted ))
                logger.info(f"{prev} -> {converted}")
            # transfer the rest of the data to make a perfect copy
            else:
                newtrack.append(event.copy())
        # append track to new midi file
        outMidi.tracks.append(newtrack)
    return outMidi

class ReHarmonizer:
    """Object to reharmonize with Negative Harmony"""
    def __init__(self, Inf: str, Outf: str, notes=1, key: str=None):

        self.inf: str = Inf
        self.outf: str = Outf
        self.notes: int = notes
        self.key: str = key
        self.outMid: object = MidiFile()
        self.convert()

    def convert(self):
        """function to convert"""
        midiFile = readIn(f=self.inf)
        midiFile = flip(midiFile=midiFile, outMidi=self.outMid, 
                        notes=self.notes, key=self.key)
        readOut(midiFile=midiFile, f=self.outf)