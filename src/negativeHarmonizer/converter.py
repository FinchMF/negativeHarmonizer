from negativeHarmonizer import ( mido, MidiFile, MidiTrack, Negator, logger )

def readIn(f: str) -> mido.midifiles.midifiles.MidiFile:
    """Function to read in MidiFile"""
    return MidiFile(f)

def readOut(midiFile: mido.midifiles.midifiles.MidiFile, f: str):
    """Function to save midifile"""
    midiFile.save(f"{f}.mid")


def flip(midiFile: mido.midifiles.midifiles.MidiFile, 
         outMidi: mido.midifiles.midifiles.MidiFile) -> mido.midifiles.midifiles.MidiFile:
    """Function to convert each midi note into its negative counterpart"""
    # transfer header data
    outMidi.type = midiFile.type
    outMidi.ticks_per_beat = midiFile.ticks_per_beat
    outMidi.charset = midiFile.charset
    converter = None
    # iterate through tracks in the midi file
    for track in midiFile.tracks:
        # per track set up the copy
        newtrack = MidiTrack()
        # iteratae through midi messages in track
        for event in track:
            # set converter based on key (this can change through out the peice)
            if event.type == 'key_signature':
                converter = Negator(key=event.key)
                newtrack.append(event.copy())
            # convert the pitch, then transfer data
            if event.type == 'note_on': # 'note_off'
                prev = event.note
                converted = converter.convert(midi_n=int(prev))
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
    def __init__(self, Inf: str, Outf: str):

        self.inf = Inf
        self.outf = Outf
        self.outMid = MidiFile()
        self.convert()

    def convert(self):
        """function to convert"""
        midiFile = readIn(f=self.inf)
        midiFile = flip(midiFile=midiFile, outMidi=self.outMid)
        readOut(midiFile=midiFile, f=self.outf)