import RPi.GPIO as GPIO
import time
from audio import AudioFile 
from datetime import datetime
import os
import sys

def record_n_play():
    stamp = str(int(datetime.utcnow().timestamp()))
    filename = f"{stamp}.wav"
    a = AudioFile(filename)
    a.record(sec=10)
    a.play_last_nine()
    a.play()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while True:
    inputValue = GPIO.input(11)
    if inputValue == False:
        print("Button pressed")
        time.sleep(0.3)
        record_n_play()
