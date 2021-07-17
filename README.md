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

### How to Install
#
    git clone git@github.com:FinchMF/negativeHarmonizer.git

<br/><br/>

### How To Run
#
Currently this is a command-line tool

    python3.7 src/generateNegatives.py <input midi file> <name you wish to call the output>

Two Things to Note:
- If your negative output has rhythmic glitches, rerun the command adding a third argument, 0
- When naming the output file, no need to add midi extenstion .mid - it is handled for you

#### Example of Adding Third Argument to Command
#

    python3.7 src/generateNegatives.py <input midi file> <name you wish to call the output> <0>
#### What Happening with the Third Argument, 0
#

By adding the 0, you are directing the application logic to detect when a midi message contains 'note_off' information. Depending on the midi file, sometimes this is needed in order to keep the piece's note lengths, thus rhythmic structure, in tact. Other files do not need this, so the application is set to default focus on only 'note_on' midi data for a pitch.  