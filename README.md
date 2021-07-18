# negativeHarmonizer
simple application to convert midi harmony into its negative counterpart
<br/><br/>

### What is Negative Harmony?
#
In short, Negative Harmony is a transpositional process that coverts harmonic content from its functional presentation in ionian modality to a functional presentation in a phrygian modaliy of the key's 5th scale degree. This transformation changes the shape of the harmonic realtionships without destabilzing them. 

Expanding on this concept, rather than limiting the scope to pitches of a key, we can use the key to define a root of a chromatic scale and perform the same operation on all twelve tones. 
<br/><br/>

### How This Looks
#


| Original Pitch | -> | Negative Pitch |
-----------------|----|-----------------
| 0 - C natural  | -> | 7 - G natural |
| 1 - Db | -> | 6 - F# |
| 2 - D natural | -> | 5 - F natural |
| 3 - Eb | -> | 4 - E natural |
| 4 - F natural | -> | 3 -  Eb | 
| 5 - F# | -> | 2  - D natural |
| 6 - Gb natural | -> | 1 - C# |
| 7 - G natural | -> | 0 - C natural |
| 8 - Ab | -> | 11 - B natural |
| 9 - A natural | -> | 10 - Bb |
| 10 - Bb | -> | 9 - A natural |
| 11 - B natural | -> | 8 - Ab |

<br/><br/>

### How The Application Works
#
The application takes a midi file as input, then converts the entire midi into a negative. It does this by iterating through each midi message, detecting if the message contains pitch information. If there is pitch information, the pitch is converted. The rest of the midi information is retained as is, in order to make an exact negative copy. The output will populate a directory titled **negatives**

<br/><br/>

### How to Install From Git
#
    git clone git@github.com:FinchMF/negativeHarmonizer.git
    pip3 install -r requirements.txt 

<br/><br/>

### How To Run if From Git
#
Move into **negativeHarmoinzer** directory, run:

    python3.7 src/generateNegatives.py -i{input midi file} -o{output midi file name} -n=1 -k=None



Things to Note:
- If your negative output has rhythmic glitches, rerun the command changing -n to 0
- When naming the output file, no need to add midi extenstion .mid - it is handled for you

### About the Arguements
#
The first two arguments are i/o, however the additional two arguments handle how note data is processed and what key the transformative axis is chosen from. 

n is default 1, meaning that the logic only focuses on midi messages indicating note_on, when n is set to 0, the logic will handle both note_on and note_off midi messages. 

k is default None, meaning that the logic will look for the key in the midi file. If the midi file does not contain data about the key, then the key of C is chosen by default. Setting the key will override what key is in the midi file, as well as override the default C if no key is in the midi file. 

### Use as Python Library
#
Currently in beta-testing

    pip install -i https://test.pypi.org/simple/ negativeHarmonizer-FinchMF==0.0.3

 #
    from negativeHarmonizer import ReHarmonizer

    MIDI = <midiFile.mid>
    negMIDI = <name of output file>

    ########################
    # Additional Arguments #
    ########################
    notes= < choose 1 or 0 > 
    # decides whether or not to read 'note_off' data | 0 = ['note_on', 'note_off], 1 = ['note_on'] | default = 1

    key = None
    # by default ReHarmonizer will find the key in the midi data.
    # secondly, if the key is note delcared in the midi data, ReHarmonier will default to C Major
    # use the key argument to choose what key ReHarmonizer pivots the negative off of
    
    ReHarmonizer(Inf=MIDI, Outf=negMIDI, notes=notes, key=key)