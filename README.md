# BigSmilez-FL-KeyScaler
FL Studio script to make the white keys on a MIDI keyboard play the scale of your choice!

## Usage instructions 
Detailed instructions available at: https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm

## Installation instructions
- Create a folder for this script in the FL Studio UserData folder `...Documents\Image-Line\FL Studio\Settings\Hardware\MyScripts`
- Copy file `device_KeyScaler.py` to this folder
- Connect your MIDI keyboard 
- Open FL Studio, goto MIDI settings
- In `Controller Type` dropdown, select `BigSmilez Key Scaler (user)`
- Enable the controller
- Voila, now the white keys C-B will start playing notes from D# Minor (Natural) scale

## How to change the root note and scale
- Open the `device_KeyScaler.py` file in text editor of your choice
- Change line numbers 41 & 42 to variables of your choice:

ROOT_NOTE = D_SHARP

SCALE = MINOR_NATURAL


# Need more help?
Drop me a line at preet@marchingbytes.com



# Follow me on socials
[Instagram](https://instagram.com/bigsmilezmusic), [SoundCloud](https://soundcloud.com/bigsmilezmusic), [BeatStars](https://www.beatstars.com/bigsmilezmusic/feed)

@bigsmilezmusic