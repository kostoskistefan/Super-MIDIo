# Super MIDIo [![version](https://img.shields.io/badge/version-1.0-red.svg)](https://semver.org)

Super MIDIo is designed to allow you to play Super Mario Bros (or any other game with simple tweaks to the code) using a MIDI controller.

## Note
This script has been tested with a python implementation of the first level of Super Mario, done by [Justin Meister](https://github.com/justinmeister/Mario-Level-1). 

His keyboard mappings are:
* Left arrow key → Move Mario to the left
* Down arrow key → Make Mario crouch
* Right arrow key → Move Mario to the right
* Letter **A** → Make Mario jump
* Letter **S** → Make Mario run / shoot fireballs

## Requirements
* Pynput
* RtMIDI
* Numpy

## Installation

Clone the repository using git clone: `https://github.com/kostoskistefan/Super-MIDIo.git`

Change to the cloned directory: `cd Super-MIDIo`

Run the command: `pip install -r requirements.txt`

Run the script: `python3 main.py`

## Key configuration
Keys can be configured in the `key_config.py` file by changing the `keys` array to suit your needs. **The ordering of the array is important**. [Here](https://pythonhosted.org/pynput/keyboard.html#pynput.keyboard.Key) you can find a list of all possible keys that can be used.

## Usage
Start the desired game (Super Mario in our case). Once started, run the script. You will be prompted to select the MIDI interface. After the selection, switch back to the game and start playing.
