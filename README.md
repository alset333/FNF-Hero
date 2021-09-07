# FNF Hero
 Utility to convert between .chart files for Clone Hero and .json files for Friday Night Funkin'

## Known Limitations and Issues
### Want to Fix
1. Does not support songs with BPM changes or Time Signature changes.
The BPM/TS for the last section will be used for the entire song.
2. Each note is mapped to one note. You cannot map a CH "open strum" to a FNF row of arrows.
The program also cannot map one CH fret to both FNF characters (such as using 0 to 3 for gf and 1 to 4 for bf to give different but similar charts)
3. Chart format has to be specified for both input and output, no auto-detection. 
4. Inserting notes and sections is messy. Actually most of the code is messy or confusing.
### Won't Fix / Can't Fix
1. CH has (sometimes many) more frets than FNF has arrows. CH also has guitar-specific controls like strum, tap, and open. This makes conversion difficult especially for clever/creative CH memes.
