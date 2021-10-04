from audio import AudioFile 
from datetime import datetime
import os
import sys

stamp = str(int(datetime.utcnow().timestamp()))
filename = f"{stamp}.wav"
a = AudioFile(filename)
#a.record()
#a.play()
a.play_last_nine()
