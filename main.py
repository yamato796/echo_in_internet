import time
import os
import sys
from audio import AudioFile 
from datetime import datetime
from pynput.keyboard import Key, Listener


def on_press(key):
    try:
        if key == key.f14:
            print('{0} pressed'.format(key))
            stamp = str(int(datetime.utcnow().timestamp()))
			filename = f"{stamp}.wav"
			a = AudioFile(filename)
			a.record(sec=10)
			a.play_last_nine()
			a.play()
            return False
    except AttributeError:
        pass

def on_release(key):
    print('{0} release'.format(key))
    #if key == Key.esc:
        # Stop listener
    return False

# Collect events until released
while(True):
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print('Next')
