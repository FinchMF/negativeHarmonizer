
from negativeHarmonizer import ( log2, pow, logger )

class Scales:

    @staticmethod
    def negativeMap() -> dict:
        """Dictionary Containing 
        Lookup Table for Negative Harmony CounterPart"""
        return {

            0:7,
            1:6,
            2:5,
            3:4,
            4:3,
            5:2,
            6:1,
            7:0,
            8:11,
            9:10,
            10:9,
            11:8
        }
    @staticmethod
    def chromaticScaleFlat() -> list:
        """List containing the Chromatic Scale"""
        return [ 'C', 'Db', 'D', 
                'Eb', 'E', 'F', 
                'Gb', 'G', 'Ab', 
                'A', 'Bb', 'B' ]

    @staticmethod
    def chromaticScaleSharp() -> list:
        """List containing the Chromatic Scale"""
        return [ 'C', 'C#', 'D', 
                'D#', 'E', 'F', 
                'F#', 'G', 'G#', 
                'A', 'A#', 'B' ]

class Converters:

    @staticmethod
    def midi2freq(midi: int) -> float:
        """Function to convert midi note to freq"""
        return round(2**((midi-69)/12)*440, 2)

    @staticmethod
    def freq2midi(freq: float) -> int:
        """Function to convert freq to midi note"""
        return round(69 + 12*log2(freq/440))

    @staticmethod
    def freq2pitch(freq: float, accidental: str) -> tuple:
        """Function to find closest pitch give a freq"""
        # if the pitch is the exact freq, then we can 
        # think of this function as a conversion tool
        # from freq to pitch name and octave
        A4: int = 440
        C0: int = A4*pow(2, -4.75)
        h: float = round(12*log2(freq/C0))
        octave: int = h // 12
        n: int = h % 12

        if 'b' in accidental:
            pitches: list = Scales.chromaticScaleFlat()
        else:
            pitches: list = Scales.chromaticScaleSharp()

        return pitches[n], octave

    @staticmethod
    def pitch2midi(pitch: str) -> int:
        """Function to convert pitchname (with ocatave) to midi number"""
        pitchName: str = pitch[:-1]
        octave: str = pitch[-1]
        midi: int = -1
        try:
            if 'b' in pitchName:
                p: str = Scales.chromaticScaleFlat().index(pitchName)
            else:
                p: str = Scales.chromaticScaleSharp().index(pitchName)
        except:
            logger.info('Invalid pitch')
            return midi
        
        midi += p + 12 * (int(octave) + 1) + 1
        return midi

class Tones:

    @staticmethod
    def setTones(scale: list, root: str) -> list:
        """Function to order the chromatic scale from the given root"""
        twelveTone: list = list(range(12))
        rootIdx: int = scale.index(root)
        rootScale: list = scale[rootIdx:] + scale[0:rootIdx]

        rootChroma: dict = {}
        for n in range(len(rootScale)):
            rootChroma[rootScale[n]]: int = twelveTone[n]

        return rootChroma

    @staticmethod
    def getKeyTones(key: str) -> dict:
        """Function that generates a key's chromatic scale"""
        if key in Scales.chromaticScaleFlat():
            return Tones.setTones(scale=Scales.chromaticScaleFlat(), root=key)

        if key in Scales.chromaticScaleSharp():
            return Tones.setTones(scale=Scales.chromaticScaleSharp(), root=key)

    @staticmethod
    def getNegativeTones(keyTone: dict, 
                        negativeTone: dict = Scales.negativeMap()) -> dict:
        """Function that returns negative mappinig of a scale"""
        scale: list = list(keyTone.keys())
        negative: dict = {}
        for pitch, tone in keyTone.items():
            negative[pitch]: str = scale[negativeTone[tone]]

        return negative

def negativeConversion(midi: int, key: str) -> int:

    if len(key) == 2:
        accidental: str = key[-1]

    else:
        accidental: str = 'natural'

    freq: float = Converters.midi2freq(midi=midi)
    pitch, octave = Converters.freq2pitch(freq=freq, accidental=accidental)
    tones: dict = Tones.getKeyTones(key=key)
    negativeTones: dict = Tones.getNegativeTones(keyTone=tones)
    try:
        negativePitch: str = f"{negativeTones[pitch]}{octave}"
    except:
        logger.info(f"{pitch} not in | {negativeTones} ")
        logger.info(f" Enharmonic Substitution Needed")

        if '#' in pitch:
            pitch: str = Scales.chromaticScaleFlat()[Scales.chromaticScaleSharp().index(pitch)]
        else:
            pitch: str = Scales.chromaticScaleSharp()[Scales.chromaticScaleFlat().index(pitch)]

        negativePitch: str = f"{negativeTones[pitch]}{octave}"


    return Converters.pitch2midi(pitch=negativePitch)

class Negator:

    def __init__(self, key: str):
        self.key: str = key

    def convert(self, midi_n: int) -> int:
        return negativeConversion(midi=midi_n, key=self.key)