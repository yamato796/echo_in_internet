import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while True:
    inputValue = GPIO.input(11)
    if inputValue == False:
        print("Button pressed")
        time.sleep(0.3)
