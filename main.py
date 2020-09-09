import numpy as np
import sys
import time
from key_config import *
from rtmidi.midiutil import open_midiinput

class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        if message[2] != 0:
            key_config.on_press(message[1])
        else:
            key_config.on_release(message[1])


port = sys.argv[1] if len(sys.argv) > 1 else None

try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

midiin.set_callback(MidiInputHandler(port_name))
